"""
NewsAPI Integration Service
"""
import requests
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import NewsArticle, Category
import logging

logger = logging.getLogger(__name__)


class NewsAPIService:
    """Service for interacting with NewsAPI"""
    
    def __init__(self):
        self.api_key = settings.NEWS_API_KEY
        self.base_url = settings.NEWS_API_BASE_URL
    
    def _make_request(self, endpoint, params):
        """Make request to NewsAPI"""
        params['apiKey'] = self.api_key
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"NewsAPI request failed: {e}")
            return None
    
    def fetch_top_headlines(self, country='us', page_size=30):
        """Fetch top headlines"""
        params = {
            'country': country,
            'pageSize': page_size,
        }
        return self._make_request('top-headlines', params)
    
    def fetch_by_category(self, category, country='us', page_size=20):
        """Fetch news by category"""
        params = {
            'country': country,
            'category': category,
            'pageSize': page_size,
        }
        return self._make_request('top-headlines', params)
    
    def search_news(self, query, sort_by='publishedAt', page_size=20):
        """Search news articles"""
        params = {
            'q': query,
            'sortBy': sort_by,
            'pageSize': page_size,
            'language': 'en',
        }
        return self._make_request('everything', params)
    
    def cache_articles(self, articles_data, category=None):
        """Cache articles in database"""
        cached_count = 0
        
        if not articles_data or articles_data.get('status') != 'ok':
            return cached_count
        
        articles = articles_data.get('articles', [])
        
        for article_data in articles:
            try:
                # Skip if no URL
                if not article_data.get('url'):
                    continue
                
                # Check if article already exists
                if NewsArticle.objects.filter(url=article_data['url']).exists():
                    continue
                
                # Get or create category
                category_obj = None
                if category:
                    category_obj, _ = Category.objects.get_or_create(
                        name=category,
                        defaults={'display_name': category.capitalize()}
                    )
                
                # Create article
                NewsArticle.objects.create(
                    title=article_data.get('title', 'No Title'),
                    description=article_data.get('description', ''),
                    content=article_data.get('content', ''),
                    url=article_data['url'],
                    image_url=article_data.get('urlToImage', ''),
                    published_at=article_data.get('publishedAt', timezone.now()),
                    source_name=article_data.get('source', {}).get('name', 'Unknown'),
                    author=article_data.get('author', ''),
                    category=category_obj,
                )
                cached_count += 1
                
            except Exception as e:
                logger.error(f"Error caching article: {e}")
                continue
        
        return cached_count
    
    def update_category_news(self, category_name):
        """Fetch and cache news for a specific category"""
        data = self.fetch_by_category(category_name)
        return self.cache_articles(data, category_name)
    
    def update_all_categories(self):
        """Update news for all categories"""
        categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
        total_cached = 0
        
        for category in categories:
            cached = self.update_category_news(category)
            total_cached += cached
            logger.info(f"Cached {cached} articles for {category}")
        
        return total_cached


def get_cached_articles(category=None, limit=30):
    """Get cached articles from database"""
    queryset = NewsArticle.objects.filter(is_active=True)
    
    if category:
        queryset = queryset.filter(category__name=category)
    
    return queryset[:limit]


def search_cached_articles(query, limit=20):
    """Search cached articles"""
    from django.db.models import Q
    
    queryset = NewsArticle.objects.filter(
        Q(title__icontains=query) | 
        Q(description__icontains=query) |
        Q(content__icontains=query),
        is_active=True
    )
    
    return queryset[:limit]


def should_refresh_cache():
    """Check if cache should be refreshed (older than 1 hour)"""
    one_hour_ago = timezone.now() - timedelta(hours=1)
    recent_articles = NewsArticle.objects.filter(cached_at__gte=one_hour_ago)
    return recent_articles.count() < 10
