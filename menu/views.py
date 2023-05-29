from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import generics
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cart,food,Foodorder
from .serializers import Food_serializer
# Create your views here.

@login_required
def add_to_cart(request,food_id):
    item = get_object_or_404(food,id = food_id)
    cart,created = Cart.objects.get_or_create(Site_user = request.user)
    order,created = Foodorder.objects.get_or_create(i_d = food_id,
                                                    price = item.final_output_price,
                                                   # picture = item.food_picture,
                                                    name = item.food_name,
                                                    order_owner = cart.Site_user)
    order.cart_used.add(cart)
    order.quantity += 1
    order.save()
    return HttpResponseRedirect(reverse("Menu items"))
    messages.success(request,"Cart updated!")


@login_required
def get_cart(request):
    cart = get_object_or_404(Cart,Site_user = request.user)
    return HttpResponse(Foodorder.objects.filter(cart_used = cart))

class Menu_items_view(generics.ListAPIView):
    serializer_class = Food_serializer
    queryset = food.objects.all()