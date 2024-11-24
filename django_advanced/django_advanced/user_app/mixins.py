from django_advanced.user_app.models import CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

UserModel = get_user_model()

class AuthorMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user.profile
        return context


class ProfileOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        profile_pk = kwargs.get('pk')
        if profile_pk and profile_pk != request.user.pk:
            raise PermissionDenied("You do not have permission to access this profile.")
        return super().dispatch(request, *args, **kwargs)