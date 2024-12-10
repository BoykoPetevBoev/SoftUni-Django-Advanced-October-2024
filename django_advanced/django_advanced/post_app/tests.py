from django.test import TestCase

# Create your tests here.
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django_advanced.post_app.models import Post
from django_advanced.user_app.models import Profile
from django.contrib.auth import get_user_model

# UserModel = get_user_model()

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
#     import pytest
# from django.urls import reverse

# @pytest.mark.django_db
# def test_posts_view(client):
#     url = reverse('posts')
#     response = client.get(url)

#     assert response.status_code == 200
#     assert b"<h1>Published Posts</h1>" in response.content 






# @pytest.fixture
# def api_client():
#     return APIClient()

# @pytest.fixture
# def user(db):
#     user = UserModel.objects.create_user(email='test@test.com', password='password123')
#     profile = Profile.objects.create(user=user)
#     return user

# @pytest.fixture
# def post(user):
#     return Post.objects.create(
#         author=user.profile,
#         title='Test Post',
#         content='This is a test post.'
#     )

# @pytest.mark.django_db
# def test_list_posts(api_client):
#     url = reverse('post-list')
#     response = api_client.get(url)
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_create_post(api_client, user):
#     api_client.force_authenticate(user=user)
#     url = reverse('post-list')
#     data = {
#         'title': 'New Post',
#         'content': 'This is a new post.',
#         'author': user.profile.id
#     }
#     response = api_client.post(url, data, format='json')
#     assert response.status_code == 201

# @pytest.mark.django_db
# def test_retrieve_post(api_client, post):
#     url = reverse('post-detail', kwargs={'pk': post.pk})
#     response = api_client.get(url)
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_update_post(api_client, user, post):
#     api_client.force_authenticate(user=user)
#     url = reverse('post-detail', kwargs={'pk': post.pk})
#     data = {
#         'title': 'Updated Post',
#         'content': 'This is an updated post.',
#         'author': user.profile.id
#     }
#     response = api_client.put(url, data, format='json')
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_delete_post(api_client, user, post):
#     api_client.force_authenticate(user=user)
#     url = reverse('post-detail', kwargs={'pk': post.pk})
#     response = api_client.delete(url)
#     assert response.status_code == 204