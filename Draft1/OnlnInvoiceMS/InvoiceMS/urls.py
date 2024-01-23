from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.client_list, name='client_list'),
    path('clients_insert/', views.clients_insert, name='clients_insert'),
    path('insertItem/', views.insertItem, name='insertItem'),
    path('item_insert/', views.item_insert, name='item_insert'),
    path('items/', views.item_list, name='item_list'),
    path('salesmen/', views.salesman_list, name='salesman_list'),
    path('orders/', views.order_list, name='order_list'),
    # Add more paths for other entities
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('payments/', views.payment_list, name='payment_list'),
    path('users/', views.user_list, name='user_list'),
]