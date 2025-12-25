from django.db import models
from django.contrib.auth.models import User


class UserPreference(models.Model):
    """User preferences for news categories"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preferences')
    preferred_categories = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Preferences"
