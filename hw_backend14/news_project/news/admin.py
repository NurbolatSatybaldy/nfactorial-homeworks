from django.contrib import admin
from .models import News, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5  # Number of extra empty forms for comments

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'has_comments')
    inlines = [CommentInline]

    def has_comments(self, obj):
        return obj.has_comments()

admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
