from django.db import models
from django.utils import timezone


class Category(models.Model):
    """News categories"""
    CATEGORY_CHOICES = [
        ('business', 'Business'),
        ('entertainment', 'Entertainment'),
        ('general', 'General'),
        ('health', 'Health'),
        ('science', 'Science'),
        ('sports', 'Sports'),
        ('technology', 'Technology'),
    ]
    
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    display_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default='📰')  # Emoji or icon class
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.display_name


class NewsArticle(models.Model):
    """Cached news articles from NewsAPI"""
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=1000, unique=True)
    image_url = models.URLField(max_length=1000, blank=True, null=True)
    published_at = models.DateTimeField()
    source_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    
    # Metadata
    cached_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['category', '-published_at']),
        ]
    
    def __str__(self):
        return self.title
    
    def get_short_description(self):
        """Return truncated description"""
        if self.description:
            return self.description[:200] + '...' if len(self.description) > 200 else self.description
        return ''
