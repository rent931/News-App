from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleListView, 
    ArticleDetailedView, 
    ArticleUpdateView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name="article_list"),
    path('articles/<int:pk>/', ArticleDetailedView.as_view(), name="article_detail"),
    path('articles/new/', ArticleCreateView.as_view(), name='article_new'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),
    
]