from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django_advanced.user_app.forms import CustomUserCreateForm, ProfileEditForm
from django_advanced.user_app.models.profile import Profile


UserModel = get_user_model()


class UserRegisterView(CreateView):
    model = UserModel
    form_class = CustomUserCreateForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')


class UserLoginView(LoginView):
    model = UserModel
    template_name='user/login.html'
    success_url = reverse_lazy('home')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    model = UserModel
    success_url = reverse_lazy('home')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'user/profile.html'
    

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'user/profile-edit.html'

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )
