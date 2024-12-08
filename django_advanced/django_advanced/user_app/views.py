from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.generics import CreateAPIView

from django_advanced.user_app.forms import CustomUserCreateForm, ProfileEditForm
from django_advanced.user_app.models.profile import Profile
from django_advanced.user_app.mixins import ProfileOwnerMixin
from django_advanced.user_app.serializers import RegisterSerializer
from django.contrib.auth import login

UserModel = get_user_model()

class RegisterApiView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer

class UserRegisterView(CreateView):
    model = UserModel
    form_class = CustomUserCreateForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(LoginView):
    model = UserModel
    template_name='user/login.html'
    success_url = reverse_lazy('home')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    model = UserModel
    success_url = reverse_lazy('home')


class UserProfileView(LoginRequiredMixin, ProfileOwnerMixin, DetailView):
    model = UserModel
    template_name = 'user/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object.profile
        return context


class ProfileEditView(LoginRequiredMixin, ProfileOwnerMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'user/profile-edit.html'

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile',
            kwargs={
                'pk': self.object.pk,
            }
        )
