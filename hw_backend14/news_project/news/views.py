from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Comment
from django.template import loader


def news_list(request):
    # View to display all news articles sorted by created_at (descending)
    news = News.objects.all().order_by('-created_at')
    template = loader.get_template('news/news_list.html')
    return HttpResponse(template.render({'news': news}, request))


def news_detail(request, id):
    # View to display detailed info about a specific news article
    news = get_object_or_404(News, id=id)
    comments = news.comments.all().order_by('-created_at')  # Get comments sorted by created_at (descending)
    template = loader.get_template('news/news_detail.html')
    return HttpResponse(template.render({'news': news, 'comments': comments}, request))


def news_create(request):
    # View to create a new news article
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        news = News.objects.create(title=title, content=content)
        return redirect('news_detail', id=news.id)
    return render(request, 'news/news_create.html')


def comment_create(request, id):
    # View to add a comment to a specific news article
    news = get_object_or_404(News, id=id)
    if request.method == "POST":
        content = request.POST.get('content')
        Comment.objects.create(news=news, content=content)
        return redirect('news_detail', id=news.id)
    return redirect('news_detail', id=id)
