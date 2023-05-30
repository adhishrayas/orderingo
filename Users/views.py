from django.shortcuts import render,get_object_or_404
from menu.models import Cart,Foodorder
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import get_cart_serializer,User_details_serializer
from Helpers import permissions
# Create your views here.

class get_cart_view(generics.ListAPIView):
    serializer_class = get_cart_serializer

    def get_queryset(self):
        return Foodorder.objects.filter(order_owner = self.request.user)


class User_account_view(generics.RetrieveUpdateAPIView):
    serializer_class = User_details_serializer
    queryset = CustomUser.objects.all()
    def get(self,request):
        serializer = User_details_serializer(request.user)
        return Response(serializer.data)

class Decrease_quantity(APIView):
  permission_classes = (permissions.IsAuthorOrReadOnly,)
  def Decrease_quantity(self,food_id):
        order = get_object_or_404(Foodorder,i_d = food_id)
        if order.quantity > 1:
            order.quantity -= 1
            order.save()
        else:
            order.delete()

        return HttpResponseRedirect(reverse("Users:Get cart"))

class Object_remove_view(APIView):
    permission_classes = (permissions.IsAuthorOrReadOnly,)

    def remove_object_from_cart(self,food_id):
       order = get_object_or_404(Foodorder,i_d = food_id)
       order.delete()
       return HttpResponseRedirect(reverse("Users:Get cart"))

class Delete_user(APIView):
  permission_classes = (permissions.IsAuthorOrReadOnly,)

  def remove_user(self,request,*args,**kwargs):
    User = self.request.user
    User.delete()
    return HttpResponseRedirect(reverse("menu:Menu items"))
     