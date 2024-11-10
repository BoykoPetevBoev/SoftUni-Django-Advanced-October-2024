from django_advanced.user_app.models import CustomUser


class AuthorMixin:
    def get_author(self):
        return CustomUser.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.get_author()
        return context
