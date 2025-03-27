from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<int:id>/', views.news_detail, name='news_detail'),
    path('new/', views.news_create, name='news_create'),
    path('<int:id>/comment/', views.comment_create, name='comment_create'),
]
