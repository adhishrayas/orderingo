from django.shortcuts import render,get_object_or_404
from menu.models import Cart,Foodorder
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from rest_framework import generics
from .serializers import get_cart_serializer,User_details_serializer
# Create your views here.

class get_cart_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = get_cart_serializer

    def get_queryset(self):
        c = get_object_or_404(Cart,Site_user = self.request.user)
        return Foodorder.objects.filter(cart_used = c)
    
class User_account_view(generics.RetrieveUpdateAPIView):
    serializer_class = User_details_serializer
    def get_queryset(self):
        return CustomUser.objects.get(id = self.request.user.id)

@login_required
def remove_from_cart(self,food_id):
        order = get_object_or_404(Foodorder,i_d = food_id)
        if order.quantity > 1:
            order.quantity -= 1
            order.save()
        else:
            order.delete()

        return HttpResponseRedirect(reverse("Users:Get cart"))

@login_required
def remove_object_from_cart(self,food_id):
     order = get_object_or_404(Foodorder,i_d = food_id)
     order.delete()
     return HttpResponseRedirect(reverse("Users:Get cart"))
