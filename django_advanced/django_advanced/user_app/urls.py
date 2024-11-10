from django.urls import path
from django_advanced.user_app import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),    
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('<int:pk>/profile/', views.UserProfileView.as_view(), name='profile'),
]
