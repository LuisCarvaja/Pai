from django.shortcuts import render
from django.http import JsonResponse


def create_checkout_session(request):
    return JsonResponse({"message": "endpoint activo"})

def subscription_status(request, customer_id):
    return JsonResponse({"message": f"status para {customer_id}"})
