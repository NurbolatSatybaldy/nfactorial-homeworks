from django.db import models
from django.contrib.auth.models import User


# News Model
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title

    # Method to check if the news has comments
    def has_comments(self):
        return self.comments.exists()


# Comment Model
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment by {self.author.username} on {self.news.title}"

