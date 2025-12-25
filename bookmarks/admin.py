from django.contrib import admin
from .models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_title', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['user__username', 'article_data']
    readonly_fields = ['created_at']
    
    def get_title(self, obj):
        return obj.get_title()
    get_title.short_description = 'Article Title'
