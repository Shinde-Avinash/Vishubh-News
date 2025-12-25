from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category_name>/', views.category_news, name='category'),
    path('article/<int:article_id>/', views.article_detail, name='detail'),
    path('search/', views.search_news, name='search'),
]
