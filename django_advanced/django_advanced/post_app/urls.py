from django.urls import include, path
from django_advanced.post_app import views


urlpatterns = [
    path('', views.ListPostPage.as_view(), name='posts'),
    path('create/', views.CreatePostPage.as_view(), name='create-post'),
    path('<int:pk>/', include([
        path('edit/', views.EditPostPage.as_view(), name='edit-post'),
        path('delete/', views.DeletePostPage.as_view(), name='delete-post'),
        path('details/', views.DetailsPostPage.as_view(), name='details-post'),
    ])),     
]
