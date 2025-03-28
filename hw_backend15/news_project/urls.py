from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Main news list => ""
    path('', views.news_list, name='news_list'),

    # Detail => "102/<news_id>/"
    path('102/<int:news_id>/', views.news_detail, name='news_detail'),

    # Add => "/add/"
    path('add/', views.news_add, name='news_add'),

    # Edit => "/edit/<news_id>/"
    path('edit/<int:news_id>/', views.NewsEditView.as_view(), name='news_edit'),

    # Delete news => "/102/<news_id>/delete/"
    path('102/<int:news_id>/delete/', views.news_delete, name='news_delete'),

    # Delete comment => "/comment/<comment_id>/delete/"
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),

    # Sign up => "/sign-up/"
    path('sign-up/', views.sign_up, name='sign_up'),

    # /login/ => built-in login view with our custom template
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

    # /logout/ => built-in logout view => no more 405 error
    path('logout/', LogoutView.as_view(), name='logout'),
]
