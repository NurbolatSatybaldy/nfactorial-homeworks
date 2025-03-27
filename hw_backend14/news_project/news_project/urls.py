from django.urls import path
from news import views

urlpatterns = [
    path('news/', views.news_list, name='news_list'),  # List of news
    path('news/<int:id>/', views.news_detail, name='news_detail'),  # Detail view of a single news
    path('news/new/', views.news_create, name='news_create'),  # Form to create a new news
]
