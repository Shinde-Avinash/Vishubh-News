from django.urls import path
from . import views

app_name = 'bookmarks'

urlpatterns = [
    path('', views.bookmark_list, name='list'),
    path('add/<int:article_id>/', views.add_bookmark, name='add'),
    path('remove/<int:bookmark_id>/', views.remove_bookmark, name='remove'),
    path('check/<int:article_id>/', views.check_bookmark, name='check'),
]
