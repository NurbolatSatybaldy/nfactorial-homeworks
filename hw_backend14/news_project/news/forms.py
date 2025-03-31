# news/forms.py

from django import forms
from .models import Comment, News

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
