from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View

from django.contrib.auth import authenticate, login

from .models import News, Comment
from .forms import NewsForm

def news_list(request):
    """
    "" => list of news, descending by created_at
    """
    all_news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': all_news})

def news_detail(request, news_id):
    """
    "102/<news_id>/" => detail page for one news
    Also handles new comment if POST.
    """
    news_item = get_object_or_404(News, pk=news_id)
    comments_db = Comment.objects.filter(news=news_item).order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST.get('content')
            Comment.objects.create(news=news_item, author=request.user, content=content)
            return redirect('news_detail', news_id=news_id)
        else:
            return HttpResponseForbidden("Доступно для авторизованных")

    # Permissions for edit/delete
    can_edit_news = False
    can_delete_news = False
    if request.user.is_authenticated:
        if news_item.author == request.user or request.user.groups.filter(name='moderators').exists():
            can_edit_news = True
            can_delete_news = True

    # build comment + can_delete
    comments_info = []
    for c in comments_db:
        can_del = False
        if request.user.is_authenticated:
            if c.author == request.user or request.user.groups.filter(name='moderators').exists():
                can_del = True
        comments_info.append((c, can_del))

    return render(request, 'news/news_detail.html', {
        'news': news_item,
        'comments_info': comments_info,
        'can_edit_news': can_edit_news,
        'can_delete_news': can_delete_news,
    })

@login_required
def news_add(request):
    """
    "/add/" => add a new news item
    after creation => redirect to its detail
    """
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            new_obj = form.save(commit=False)
            new_obj.author = request.user
            new_obj.save()
            return redirect('news_detail', news_id=new_obj.id)
    else:
        form = NewsForm()
    return render(request, 'news/news_add.html', {'form': form})

class NewsEditView(View):
    """
    "/edit/<news_id>/" => GET => show form, POST => save => redirect to detail
    """
    def get(self, request, news_id):
        news_item = get_object_or_404(News, pk=news_id)
        # must be author or in 'moderators'
        if news_item.author != request.user and not request.user.groups.filter(name='moderators').exists():
            return HttpResponseForbidden("You do not have permission to edit.")
        form = NewsForm(instance=news_item)
        return render(request, 'news/news_edit.html', {
            'form': form,
            'news_item': news_item,
        })

    def post(self, request, news_id):
        news_item = get_object_or_404(News, pk=news_id)
        if news_item.author != request.user and not request.user.groups.filter(name='moderators').exists():
            return HttpResponseForbidden("You do not have permission to edit.")
        form = NewsForm(request.POST, instance=news_item)
        if form.is_valid():
            form.save()
            return redirect('news_detail', news_id=news_id)
        return render(request, 'news/news_edit.html', {
            'form': form,
            'news_item': news_item,
        })

@login_required
def news_delete(request, news_id):
    """
    "/102/<news_id>/delete/" => delete if user is author or in 'moderators'
    """
    news_item = get_object_or_404(News, pk=news_id)
    if news_item.author == request.user or request.user.groups.filter(name='moderators').exists():
        news_item.delete()
        return redirect('news_list')
    else:
        return HttpResponseForbidden("You do not have permission to delete this news.")

@login_required
def comment_delete(request, comment_id):
    """
    "/comment/<comment_id>/delete/" => delete comment if user is author or in 'moderators'
    """
    c = get_object_or_404(Comment, pk=comment_id)
    if c.author == request.user or request.user.groups.filter(name='moderators').exists():
        n_id = c.news.id
        c.delete()
        return redirect('news_detail', news_id=n_id)
    else:
        return HttpResponseForbidden("You do not have permission to delete this comment.")

def sign_up(request):
    """
    "/sign-up/" => create user => place them in 'default' group => redirect to /login/
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            default_group, _ = Group.objects.get_or_create(name='default')
            Group.objects.get_or_create(name='moderators')
            user.groups.add(default_group)
            return redirect('login')  # => /login/
    else:
        form = UserCreationForm()
    return render(request, 'registration/sign_up.html', {'form': form})
