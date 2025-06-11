from django.shortcuts import render
import stripe
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Subscriber  # Ajusta si tu modelo tiene otro nombre
from django.views.decorators.http import require_GET

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")

            if not name or not email:
                return JsonResponse({"error": "Nombre y correo son obligatorios"}, status=400)

            # 1. Crear el cliente en Stripe
            customer = stripe.Customer.create(
                name=name,
                email=email,
            )

            # 2. Crear o recuperar el suscriptor local
            subscriber, created = Subscriber.objects.get_or_create(
                email=email,
                defaults={
                    "name": name,
                    "customer_id": customer.id
                }
            )

            # 3. Si ya existe pero con otro customer_id, actualízalo
            if not created:
                subscriber.customer_id = customer.id
                subscriber.name = name
                subscriber.save()

            # 4. Crear la sesión de Checkout para suscripción
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                mode="subscription",
                customer=customer.id,
                line_items=[{
                    "price": "price_1RYZDHDQVinpXJhYhNoMXxo4",  # Ajusta según tu Stripe
                    "quantity": 1,
                }],
                success_url="http://localhost:5173/dashboard?session_id={CHECKOUT_SESSION_ID}",
                cancel_url="http://localhost:5173/",
            )

            return JsonResponse({"url": session.url})

        except Exception as e:
            return JsonResponse({"error": f"Error al crear sesión: {str(e)}"}, status=500)

@require_GET
def subscription_status(request, customer_id):
    try:
        subscriptions = stripe.Subscription.list(customer=customer_id)

        if subscriptions.data:
            status = subscriptions.data[0].status
        else:
            status = "inactive"

        return JsonResponse({
            "customer_id": customer_id,
            "status": status,
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
    
@require_GET
def subscription_status_by_session(request, session_id):
    try:
        session = stripe.checkout.Session.retrieve(session_id)

        customer_id = session.customer

        if not customer_id:
            return JsonResponse({"error": "Cliente no encontrado"}, status=404)

        subscriptions = stripe.Subscription.list(customer=customer_id)

        status = subscriptions.data[0].status if subscriptions.data else "inactive"

        subscriber = Subscriber.objects.filter(customer_id=customer_id).first()

        return JsonResponse({
            "name": subscriber.name if subscriber else None,
            "email": subscriber.email if subscriber else session.customer_details.email,
            "status": status
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
