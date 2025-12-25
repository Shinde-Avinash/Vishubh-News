from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Bookmark
from news.models import NewsArticle


@login_required
def bookmark_list(request):
    """Display user's bookmarks"""
    bookmarks = Bookmark.objects.filter(user=request.user)
    
    context = {
        'bookmarks': bookmarks,
        'page_title': 'My Bookmarks',
    }
    return render(request, 'bookmarks/list.html', context)


@login_required
def add_bookmark(request, article_id):
    """Add article to bookmarks"""
    article = get_object_or_404(NewsArticle, id=article_id)
    
    # Check if already bookmarked
    if Bookmark.objects.filter(user=request.user, article_url=article.url).exists():
        messages.info(request, 'Article already bookmarked.')
    else:
        # Create bookmark
        article_data = {
            'title': article.title,
            'description': article.description,
            'url': article.url,
            'image_url': article.image_url,
            'source_name': article.source_name,
            'published_at': str(article.published_at),
        }
        
        Bookmark.objects.create(
            user=request.user,
            article_url=article.url,
            article_data=article_data
        )
        messages.success(request, 'Article bookmarked successfully!')
    
    return redirect('news:detail', article_id=article.id)


@login_required
def remove_bookmark(request, bookmark_id):
    """Remove bookmark"""
    bookmark = get_object_or_404(Bookmark, id=bookmark_id, user=request.user)
    bookmark.delete()
    messages.success(request, 'Bookmark removed.')
    return redirect('bookmarks:list')


@login_required
def check_bookmark(request, article_id):
    """Check if article is bookmarked (AJAX endpoint)"""
    article = get_object_or_404(NewsArticle, id=article_id)
    is_bookmarked = Bookmark.objects.filter(
        user=request.user, 
        article_url=article.url
    ).exists()
    
    return JsonResponse({'is_bookmarked': is_bookmarked})
