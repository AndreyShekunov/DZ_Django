from django.urls import path
from . import views

urlpatterns = [
    path('clients/create/', views.create_client, name='create_client'),
    path('clients/', views.get_all_clients, name='get_all_clients'),
    path('clients/<int:client_id>/update/', views.update_client, name='update_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),

    path('products/create/', views.create_product, name='create_product'),
    path('products/', views.get_all_products, name='get_all_products'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),

    path('orders/create/', views.create_order, name='create_order'),
    path('orders/', views.get_all_orders, name='get_all_orders'),
    path('orders/<int:order_id>/update/', views.update_order, name='update_order'),
    path('orders/<int:order_id>/delete/', views.delete_order, name='delete_order'),

    path('', views.index, name='index'),
]