from django.test import TestCase
import pytest
from django.urls import reverse
from django.test import Client

# @pytest.mark.django_db
# def test_user_list_view():
#     client = Client()
#     response = client.get(reverse('restlogin'))
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_user_detail_view(user):
#     client = Client()
#     response = client.get(reverse('user-detail', kwargs={'pk': user.id}))
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_user_create_view():
#     client = Client()
#     response = client.post(reverse('user-create'), {
#         'username': 'testuser',
#         'password': 'password123',
#         'email': 'testuser@example.com'
#     })
#     assert response.status_code == 302

# @pytest.mark.django_db
# def test_user_update_view(user):
#     client = Client()
#     response = client.post(reverse('user-update', kwargs={'pk': user.id}), {
#         'username': 'updateduser',
#         'email': 'updateduser@example.com'
#     })
#     assert response.status_code == 302

# @pytest.mark.django_db
# def test_user_delete_view(user):
#     client = Client()
#     response = client.post(reverse('user-delete', kwargs={'pk': user.id}))
#     assert response.status_code == 302