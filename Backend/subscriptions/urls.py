from django.urls import path
from . import views

urlpatterns = [
    path('create-checkout-session/', views.create_checkout_session),
    path('subscription-status/<str:customer_id>/', views.subscription_status),
]
