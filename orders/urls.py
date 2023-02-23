from django.urls import path

from orders.views import (CancelledTemplateView, OrderCreateView,
                          OrderDetailView, OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order-success'),
    path('order-cancelled/', CancelledTemplateView.as_view(), name='order-cancelled'),
    path('', OrderListView.as_view(), name='orders-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
