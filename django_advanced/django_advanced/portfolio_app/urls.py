from django.urls import include, path
from django_advanced.portfolio_app import views


urlpatterns = [
    path('', views.ListPortfolioPage.as_view(), name='portfolio-list'),
    path('create/', views.CreatePortfolioPage.as_view(), name='create-portfolio'),
    path('<int:pk>/', include([
        path('', views.DetailsPortfolioPage.as_view(), name='details-portfolio'),
        path('edit/', views.EditPortfolioPage.as_view(), name='edit-portfolio'),
        path('delete/', views.DeletePortfolioPage.as_view(), name='delete-portfolio'),
    ])),     
]
