from django.conf import settings  # Add this line
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),  # Include the news URLs
]

# Only include the debug toolbar in debug mode
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),  # Add this line
    ] + urlpatterns
