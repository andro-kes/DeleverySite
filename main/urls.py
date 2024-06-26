from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='detail'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('create/', views.CreateOrderView.as_view(), name='create'),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('order_product', views.order_product, name='order_product'),
]
