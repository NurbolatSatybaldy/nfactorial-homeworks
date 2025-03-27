from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News
from datetime import datetime

def news_create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        created_at = datetime.now()

        news = News.objects.create(title=title, content=content, created_at=created_at)

        return redirect('news_detail', id=news.id)

    return render(request, 'news/news_create.html')

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, id):
    try:
        news = News.objects.get(id=id)
    except News.DoesNotExist:
        return HttpResponse("News not found", status=404)

    return render(request, 'news/news_detail.html', {'news': news})
