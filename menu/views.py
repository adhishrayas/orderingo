from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import generics
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cart,food,Foodorder
from .serializers import Food_serializer,Food_detail_serializer
# Create your views here.


class Menu_items_view(generics.ListAPIView):
    serializer_class = Food_serializer
    queryset = food.objects.all()

   
class Menu_item_detail_view(generics.RetrieveUpdateAPIView):
    serializer_class = Food_detail_serializer
    queryset = food.objects.all()

    def update(self, request, pk, **kwargs):
        item = get_object_or_404(food,pk = pk)
        cart,created = Cart.objects.get_or_create(Site_user = request.user)
        order,created = Foodorder.objects.get_or_create(i_d = pk,
                                                    price = item.final_output_price,
                                                    picture = item.food_picture,
                                                    name = item.food_name,
                                                    order_owner = request.user)
        order.cart_used.add(cart)
        order.quantity += 1
        order.save()
        return HttpResponseRedirect(reverse("menu:details"))

