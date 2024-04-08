from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='detail'),
]
