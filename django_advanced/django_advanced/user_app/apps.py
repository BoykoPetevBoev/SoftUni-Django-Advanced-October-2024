from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_advanced.user_app'

    def ready(self):
        import django_advanced.user_app.signals