from django.contrib import admin
from .models import News, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5  # Allows adding 5 extra comment fields

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'has_comments')
    inlines = [CommentInline]

admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
