import stripe
from decimal import Decimal
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from menu.models import Foodorder
from rest_framework import generics,status
# Create your views here.

@api_view(['POST'])
def secret(request,formal = None):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
        user = request.data.get('user')
        Food_orders = Foodorder.objects.filter(order_owner = user)
        
        subtotal = []
        for f in Food_orders:
            food_id = f.get('i_d')
            qty = f.get('quantity')
            F = Foodorder.objects.get(i_d = food_id)
            subtotal.append(F.price*qty)
        
        total = round(Decimal(sum(subtotal)),2)
        stripe_total = int(total*100)
        intent = stripe.PaymentIntent.create(
            amount = stripe_total,
            currency = "rs",
            automatic_payment_methods = {"enabled":True},
        )
        return Response(data = {
            'client_secret':intent.client_secret
        },status=status.HTTP_201_CREATED)
    return Response(status = status.HTTP_400_BAD_REQUEST)
    
    
