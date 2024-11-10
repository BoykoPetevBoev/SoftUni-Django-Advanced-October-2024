from django_advanced.user_app.forms import CustomUserForm
from django.views.generic import CreateView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')


class UserLoginView(LoginView):
    template_name='user/login.html'
    success_url = reverse_lazy('home')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name='user/logout.html'
    success_url = reverse_lazy('home')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template = 'user/profile.html'