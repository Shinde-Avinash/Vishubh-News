import feedparser
from datetime import datetime
from time import mktime
import logging
from django.utils.timezone import make_aware, now

logger = logging.getLogger(__name__)

class NewsAPIService:
    """
    Service to fetch news from RSS feeds and save to database.
    Replaces the previous static API service.
    """
    
    # RSS Feed Configuration
    FEEDS = {
        'general': [
            'http://feeds.bbci.co.uk/news/rss.xml',
            'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
            'https://feeds.npr.org/1001/rss.xml',
        ],
        'technology': [
            'http://feeds.bbci.co.uk/news/technology/rss.xml',
            'https://techcrunch.com/feed/',
            'https://www.theverge.com/rss/index.xml',
        ],
        'business': [
            'http://feeds.bbci.co.uk/news/business/rss.xml',
            'https://www.cnbc.com/id/10001147/device/rss/rss.html',
            'https://feeds.npr.org/1006/rss.xml',
        ],
        'sports': [
            'http://feeds.bbci.co.uk/sport/rss.xml',
            'https://www.espn.com/espn/rss/news',
        ],
        'entertainment': [
            'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml',
            'https://www.hollywoodreporter.com/feed/',
        ],
        'health': [
            'http://feeds.bbci.co.uk/news/health/rss.xml',
            'https://www.npr.org/rss/rss.php?id=1128',
        ],
        'science': [
            'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
            'https://www.sciencedaily.com/rss/top_news.xml',
        ]
    }

    def update_all_categories(self):
        """Fetch news for all categories and save to DB. Returns count of new articles."""
        from .models import NewsArticle, Category
        
        total_new = 0
        categories = Category.objects.all()
        
        for category in categories:
            try:
                result = self.fetch_top_headlines(category=category.name)
                articles = result.get('articles', [])
                
                for article_data in articles:
                   if self._save_article(article_data, category):
                       total_new += 1
                       
            except Exception as e:
                logger.error(f"Error updating category {category.name}: {e}")
                
        return total_new

    def fetch_top_headlines(self, country='us', category=None):
        """Fetch top headlines from RSS feeds."""
        category_key = category.lower() if category else 'general'
        # Fallback to general if category not found
        feeds = self.FEEDS.get(category_key, self.FEEDS.get('general'))
        
        all_articles = []
        
        for feed_url in feeds:
            try:
                feed = feedparser.parse(feed_url)
                
                # Limit validation
                entries = feed.entries[:10] if hasattr(feed, 'entries') else []
                
                for entry in entries:
                    article = self._parse_entry(entry, feed.feed.get('title', 'Unknown Source'))
                    if article:
                        all_articles.append(article)
                        
            except Exception as e:
                logger.error(f"Error fetching RSS feed {feed_url}: {e}")
                continue
                
        # Sort by date (newest first)
        all_articles.sort(key=lambda x: x['publishedAt'] or '', reverse=True)
        return {'articles': all_articles}

    def _parse_entry(self, entry, source_name):
        """Parse a single RSS entry into the expected dict format"""
        try:
            # Handle date parsing
            published_at = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                dt = datetime.fromtimestamp(mktime(entry.published_parsed))
                published_at = make_aware(dt).isoformat()
            else:
                published_at = make_aware(datetime.now()).isoformat()
            
            # extract image
            image_url = None
            if hasattr(entry, 'media_content') and len(entry.media_content) > 0:
                image_url = entry.media_content[0]['url']
            elif hasattr(entry, 'media_thumbnail') and len(entry.media_thumbnail) > 0:
                image_url = entry.media_thumbnail[0]['url']
            elif hasattr(entry, 'links'):
                for link in entry.links:
                    if link.type.startswith('image/'):
                        image_url = link.href
                        break
            
            # If no image found, check enclosure
            if not image_url and hasattr(entry, 'enclosures'):
                 for enclosure in entry.enclosures:
                    if enclosure.type.startswith('image/'):
                        image_url = enclosure.href
                        break

            # Fallback for empty title/url
            if not entry.get('title') or not entry.get('link'):
                return None

            return {
                'title': entry.get('title'),
                'description': entry.get('summary', '')[:500], # Limit summary length
                'url': entry.get('link'),
                'urlToImage': image_url,
                'publishedAt': published_at,
                'source': {'name': source_name}
            }
        except Exception as e:
            logger.error(f"Error parsing entry: {e}")
            return None

    def _save_article(self, data, category):
        """Save a single article to the database"""
        from .models import NewsArticle
        try:
            # Check for duplicates by URL
            if NewsArticle.objects.filter(url=data['url']).exists():
                return False
                
            NewsArticle.objects.create(
                title=data['title'],
                description=data.get('description', ''),
                url=data['url'],
                image_url=data.get('urlToImage'),
                published_at=data['publishedAt'],
                source_name=data['source']['name'],
                category=category
            )
            return True
        except Exception as e:
            logger.error(f"Error saving article {data.get('title')}: {e}")
            return False

    def search_news(self, query, sort_by='publishedAt', page_size=20):
        """Search fallback."""
        logger.warning("Search not natively supported by RSS. Returning general headlines.")
        return self.fetch_top_headlines()

def should_refresh_cache():
    """Check if we should fetch new data (e.g. if latest news is > 15 mins old)"""
    from .models import NewsArticle
    from django.utils import timezone
    from datetime import timedelta
    
    last_article = NewsArticle.objects.order_by('-cached_at').first()
    if not last_article:
        return True
        
    # Refresh if older than 15 minutes
    return timezone.now() - last_article.cached_at > timedelta(minutes=15)
