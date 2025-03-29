from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django_advanced.post_app.models import Post
from django_advanced.user_app.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_list_posts(client):
    url = reverse('post-list')
    response = client.get(url)
    assert response.status_code == 200
    assert b'Published Posts' in response.content 


@pytest.mark.django_db
def test_create_post(client):
    user = User.objects.create_user(email='test@test.com', password='testpassword')
    profile = Profile.objects.create(user=user)  # Example profile model
    client.force_authenticate(user=user)
    url = reverse('edit-post')
    response = client.get(url)
    assert response.status_code == 200
    assert b'Edit Posts' in response.content 


@pytest.mark.django_db
def test_retrieve_post(client):
    user = User.objects.create_user(email='test@test.com', password='testpassword')
    profile = Profile.objects.create(user=user)  # Example profile model
    post = Post.objects.create(title='Test Post', description='This is a test post.', author=user.profile)
    url = reverse('details-post', kwargs={'pk': post.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert b'Post Details' in response.content 

# @pytest.mark.django_db
# def test_update_post(client, user, post):
#     client.force_authenticate(user=user)
#     url = reverse('details-post', kwargs={'pk': post.pk})
#     data = {
#         'title': 'Updated Post',
#         'content': 'This is an updated post.',
#         'author': user.profile.id
#     }
#     response = client.put(url, data, format='json')
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_delete_post(client, user, post):
#     client.force_authenticate(user=user)
#     url = reverse('details-post', kwargs={'pk': post.pk})
#     response = client.delete(url)
#     assert response.status_code == 204