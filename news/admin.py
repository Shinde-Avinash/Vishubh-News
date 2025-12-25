from django.contrib import admin
from .models import Category, NewsArticle


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_name', 'icon']
    search_fields = ['name', 'display_name']


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'source_name', 'category', 'published_at', 'cached_at']
    list_filter = ['category', 'source_name', 'published_at', 'is_active']
    search_fields = ['title', 'description', 'source_name']
    date_hierarchy = 'published_at'
    readonly_fields = ['cached_at', 'updated_at']
    
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'description', 'content', 'author')
        }),
        ('Source & Links', {
            'fields': ('source_name', 'url', 'image_url')
        }),
        ('Classification', {
            'fields': ('category', 'published_at')
        }),
        ('Metadata', {
            'fields': ('is_active', 'cached_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['deactivate_articles', 'activate_articles']
    
    def deactivate_articles(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_articles.short_description = "Deactivate selected articles"
    
    def activate_articles(self, request, queryset):
        queryset.update(is_active=True)
    activate_articles.short_description = "Activate selected articles"
