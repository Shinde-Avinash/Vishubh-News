from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import NewsArticle, Category
from .rss_service import NewsAPIService, should_refresh_cache
import logging

logger = logging.getLogger(__name__)


def home(request):
    """Homepage - Display top headlines"""
    # Check if cache needs refresh
    if should_refresh_cache():
        try:
            service = NewsAPIService()
            service.update_all_categories()
        except Exception as e:
            logger.error(f"Error refreshing cache: {e}")
    
    # Get articles
    articles = NewsArticle.objects.filter(is_active=True).select_related('category')[:30]
    categories = Category.objects.all()
    
    context = {
        'articles': articles,
        'categories': categories,
        'page_title': 'Latest News',
    }
    return render(request, 'news/home.html', context)


def category_news(request, category_name):
    """Display news by category"""
    category = get_object_or_404(Category, name=category_name)
    
    # Get category articles
    articles = NewsArticle.objects.filter(
        category=category, 
        is_active=True
    ).select_related('category')
    
    # Pagination
    paginator = Paginator(articles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'category': category,
        'articles': page_obj,
        'categories': categories,
        'page_title': f'{category.display_name} News',
    }
    return render(request, 'news/category.html', context)


def article_detail(request, article_id):
    """Display article details"""
    article = get_object_or_404(NewsArticle, id=article_id, is_active=True)
    
    # Get related articles (same category)
    related_articles = NewsArticle.objects.filter(
        category=article.category,
        is_active=True
    ).exclude(id=article.id)[:6]
    
    categories = Category.objects.all()
    
    context = {
        'article': article,
        'related_articles': related_articles,
        'categories': categories,
        'page_title': article.title,
    }
    return render(request, 'news/detail.html', context)


def search_news(request):
    """Search news articles"""
    query = request.GET.get('q', '').strip()
    articles = []
    
    if query:
        articles = NewsArticle.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(content__icontains=query),
            is_active=True
        ).select_related('category')
        
        # Pagination
        paginator = Paginator(articles, 20)
        page_number = request.GET.get('page')
        articles = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'articles': articles,
        'query': query,
        'categories': categories,
        'page_title': f'Search Results for "{query}"',
    }
    return render(request, 'news/search.html', context)
