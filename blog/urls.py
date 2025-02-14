from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView

app_name = 'blog'

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('add/', BlogPostCreateView.as_view(), name='blog_add'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='blog_edit'),
]
