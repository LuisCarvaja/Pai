from django.urls import path
from . import views

urlpatterns = [
    path('create-checkout-session/', views.create_checkout_session),
    path('subscription-status/<str:customer_id>/', views.subscription_status),
    path('subscription-status-by-session/<str:session_id>/', views.subscription_status_by_session),

]
