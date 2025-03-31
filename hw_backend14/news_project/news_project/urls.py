# news_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),  # Include news app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Login, logout, password reset
]
