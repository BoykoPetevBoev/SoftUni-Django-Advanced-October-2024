from django.urls import path, include
from django_advanced.user_app import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),    
    path('profile/<int:pk>/', include([
        path('', views.UserProfileView.as_view(), name='profile'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    ])),
    path('rest/', include([
        path('login/', ObtainAuthToken.as_view(), name='rest-login'),
        path('register/', views.RegisterApiView.as_view(), name='rest-register'),
    ]))
]
