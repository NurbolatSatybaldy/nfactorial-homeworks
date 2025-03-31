from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import News, Comment

class NewsModelTest(TestCase):

    def test_has_comments_false(self):
        user = User.objects.create_user(username='u1', password='pass')
        news = News.objects.create(title='No Comment News', content='Test content', author=user)
        self.assertFalse(news.has_comments())

    def test_has_comments_true(self):
        user = User.objects.create_user(username='u1', password='pass')
        news = News.objects.create(title='Has Comment News', content='Test content', author=user)
        Comment.objects.create(content='A comment', news=news, author=user)
        self.assertTrue(news.has_comments())


class NewsViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass')
        self.news1 = News.objects.create(title='First News', content='Content 1', author=self.user)
        self.news2 = News.objects.create(title='Second News', content='Content 2', author=self.user)

    def test_list_descending(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        news_list = response.context['news']
        self.assertEqual(news_list[0], self.news2)  # newer one first
        self.assertEqual(news_list[1], self.news1)

    def test_detail_view(self):
        response = self.client.get(reverse('news_detail', args=[self.news1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'First News')

    def test_comments_descending(self):
        Comment.objects.create(content='Old comment', news=self.news1, author=self.user)
        Comment.objects.create(content='New comment', news=self.news1, author=self.user)
        response = self.client.get(reverse('news_detail', args=[self.news1.id]))
        comments = response.context['comments']
        self.assertEqual(comments[0].content, 'New comment')
        self.assertEqual(comments[1].content, 'Old comment')
