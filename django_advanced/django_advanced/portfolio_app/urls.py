from django.urls import include, path
from django_advanced.portfolio_app import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.PortfolioViewSet)

urlpatterns = [
    path('', views.ListPortfolioPage.as_view(), name='portfolio'),
    path('create/', views.CreatePortfolioPage.as_view(), name='create-portfolio'),
    path('<int:pk>/', include([
        path('', views.DetailsPortfolioPage.as_view(), name='details-portfolio'),
        path('edit/', views.EditPortfolioPage.as_view(), name='edit-portfolio'),
        path('delete/', views.DeletePortfolioPage.as_view(), name='delete-portfolio'),
        path('daily-price-save/', views.daily_price_functionality, name='daily-price-save'),
    ])),     
    # path('rest/', include(router.urls)),
]
