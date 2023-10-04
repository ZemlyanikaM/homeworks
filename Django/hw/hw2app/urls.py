from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products, name='products'),
    path('clients/', views.clients, name='clients'),
    path('orders/', views.orders, name='orders'),

]

