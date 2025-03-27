from django.test import TestCase
from django.urls import reverse
from .models import News, Comment

class NewsModelTests(TestCase):

    def setUp(self):
        self.news1 = News.objects.create(title="Test News 1", content="Content of news 1")
        self.news2 = News.objects.create(title="Test News 2", content="Content of news 2")

    def test_has_comments_true(self):
        Comment.objects.create(news=self.news1, content="This is a comment")
        self.assertTrue(self.news1.has_comments())

    def test_has_comments_false(self):
        self.assertFalse(self.news2.has_comments())

class NewsViewsTests(TestCase):

    def setUp(self):
        self.news1 = News.objects.create(title="Test News 1", content="Content of news 1")
        self.news2 = News.objects.create(title="Test News 2", content="Content of news 2")
        self.comment1 = Comment.objects.create(news=self.news1, content="Comment for news 1")

    def test_news_list_view(self):
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test News 1")
        self.assertContains(response, "Test News 2")
        self.assertQuerysetEqual(
            response.context['news'],
            [repr(self.news2), repr(self.news1)],
            ordered=False
        )

    def test_news_detail_view(self):
        response = self.client.get(reverse('news_detail', args=[self.news1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test News 1")
        self.assertContains(response, "This is a comment")

    def test_comment_creation_view(self):
        response = self.client.post(reverse('comment_create', args=[self.news1.id]), data={'content': 'New comment'})
        self.assertEqual(response.status_code, 302)  # Should redirect after comment creation
        self.assertContains(response, "New comment")
