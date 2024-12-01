from django.apps import AppConfig
"""
This module defines the configuration for the 'post_app' application.
Classes:
    PostAppConfig(AppConfig): Configuration class for the 'post_app' application.
"""


class PostAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_advanced.post_app'
