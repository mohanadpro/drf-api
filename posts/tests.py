from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='mohanad', password='Mudct(4)uog')
    
    def test_can_list_posts(self):
        mohanad = User.objects.get(username='mohanad')
        Post.objects.create(owner=mohanad, title='title3')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_user_can_create_post(self):
        self.client.login(username='mohanad', password='Mudct(4)uog')
        respose = self.client.post('/posts/', {'title': 'title5','content':'content5'})
        self.assertEqual(respose.status_code, status.HTTP_201_CREATED)

    def test_not_logged_in_user_create_post(self):
        respose = self.client.post('/posts/', {'title':'title6','content':'content6'})
        self.assertEqual(respose.status_code, status.HTTP_403_FORBIDDEN)

class PostDetailsViewTest(APITestCase):
    def setUp(self):
        mohanad = User.objects.create_user(username='mohanad', password='Mudct(4)uog')
        may = User.objects.create_user(username='may', password='pass')
        Post.objects.create(owner=mohanad, title='title 7', content='content 7')
        Post.objects.create(owner=may, title='title 8', content='content8')

    
    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1')
        self.assertEqual(response.data['title'], 'title 7')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_id(self):
        response = self.client.get('/posts/5')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_post(self):
        self.client.login(username='mohanad', password='Mudct(4)uog')
        response = self.client.put('/posts/1', {'title':'new title', 'content':'new content'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title,'new title')
    
    def test_update_another_post(self):
        self.client.login(username='mohanad', password='Mudct(4)uog')
        response = self.client.put('/posts/2', {'title':'new title', 'content':'new content'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)