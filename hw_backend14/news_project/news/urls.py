# news/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:id>/', views.news_detail, name='news_detail'),
    path('new/', views.news_create, name='news_create'),
    path('<int:id>/edit/', views.NewsUpdateView.as_view(), name='news_edit'),
    path('<int:id>/delete/', views.news_delete, name='news_delete'),
    path('sign-up/', views.signup, name='sign_up'),  # Registration URL
]
