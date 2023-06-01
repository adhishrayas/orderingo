from rest_framework import serializers
from menu.models import Foodorder
from .models import CustomUser
from menu.models import Foodorder

def get_object(self):
    return self.request.user

class get_cart_serializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField("get_total_cost")
    def get_total_cost(self,*args, **kwargs):
        return sum(Food_order.cost for Food_order in Foodorder.objects.filter(order_owner = get_object(self)))
    class Meta:
        model = Foodorder
        fields = ["i_d","order_owner","name","price","quantity","picture","total_cost"]

class User_details_serializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["email","Profile_picture"]