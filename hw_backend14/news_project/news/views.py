# news/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import News, Comment
from .forms import NewsForm, CommentForm


# Sign up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'news/signup.html', {'form': form})


# News List View
def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})


# News Detail View
def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    comments = Comment.objects.filter(news=news_item).order_by('-created_at')

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.author = request.user
            comment.save()
            return redirect('news_detail', id=id)
    else:
        form = CommentForm()

    return render(request, 'news/news_detail.html', {'news_item': news_item, 'comments': comments, 'form': form})


# News Create View
@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', id=news.id)
    else:
        form = NewsForm()
    return render(request, 'news/news_create.html', {'form': form})


# News Update View (Class-Based View)
class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        if news.author != self.request.user:
            return HttpResponseForbidden("You are not authorized to edit this news.")
        news.save()
        return redirect('news_detail', id=news.id)


# News Delete View
@login_required
def news_delete(request, id):
    news_item = get_object_or_404(News, id=id)
    if news_item.author == request.user or request.user.is_staff:
        news_item.delete()
        return redirect('news_list')
    return HttpResponseForbidden("You are not authorized to delete this news.")
