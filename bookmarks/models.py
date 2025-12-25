from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):
    """User bookmarked articles"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    article_url = models.URLField(max_length=1000)
    article_data = models.JSONField()  # Store article details
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'article_url']
    
    def __str__(self):
        return f"{self.user.username} - {self.article_data.get('title', 'No Title')}"
    
    def get_title(self):
        return self.article_data.get('title', 'No Title')
    
    def get_description(self):
        return self.article_data.get('description', '')
    
    def get_image_url(self):
        return self.article_data.get('image_url', '')
    
    def get_source(self):
        return self.article_data.get('source_name', 'Unknown')
