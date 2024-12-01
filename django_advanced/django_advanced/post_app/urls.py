from django.urls import include, path
from django_advanced.post_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    path('', views.ListPostPage.as_view(), name='posts'),
    path('create/', views.CreatePostPage.as_view(), name='create-post'),
    path('<int:pk>/', include([
        path('', views.DetailsPostPage.as_view(), name='details-post'),
        path('edit/', views.EditPostPage.as_view(), name='edit-post'),
        path('delete/', views.DeletePostPage.as_view(), name='delete-post'),
        path('like/', views.likes_functionality, name='like-post'),
        path('comment/', views.comment_functionality, name='comment-post'),
    ])),
    path('rest/', include(router.urls)),
]
