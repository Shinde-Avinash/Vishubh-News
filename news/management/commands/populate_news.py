"""
Django management command to populate categories and fetch initial news
Usage: python manage.py populate_news
"""
from django.core.management.base import BaseCommand
from news.models import Category
from news.rss_service import NewsAPIService


class Command(BaseCommand):
    help = 'Populate categories and fetch initial news from NewsAPI'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting news population...'))
        
        # Create categories
        categories_data = [
            ('business', 'Business', 'Latest business and financial news', '💼'),
            ('entertainment', 'Entertainment', 'Entertainment and celebrity news', '🎬'),
            ('general', 'General', 'General news and current affairs', '📰'),
            ('health', 'Health', 'Health and medical news', '⚕️'),
            ('science', 'Science', 'Science and research news', '🔬'),
            ('sports', 'Sports', 'Sports news and updates', '⚽'),
            ('technology', 'Technology', 'Technology and innovation news', '💻'),
        ]
        
        self.stdout.write('Creating categories...')
        for name, display_name, description, icon in categories_data:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={
                    'display_name': display_name,
                    'description': description,
                    'icon': icon,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created category: {display_name}'))
            else:
                self.stdout.write(f'  - Category already exists: {display_name}')
        
        # Fetch news from API
        self.stdout.write('\nFetching news from NewsAPI...')
        service = NewsAPIService()
        
        try:
            total_cached = service.update_all_categories()
            self.stdout.write(self.style.SUCCESS(f'\n✓ Successfully cached {total_cached} articles'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'\n✗ Error fetching news: {e}'))
            self.stdout.write(self.style.WARNING('Make sure you have set NEWS_API_KEY in your .env file'))
        
        self.stdout.write(self.style.SUCCESS('\n✓ News population completed!'))
