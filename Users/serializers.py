from rest_framework import serializers
from menu.models import Foodorder
from .models import CustomUser
from menu.models import Foodorder

class get_cart_serializer(serializers.ModelSerializer):

    class Meta:
        model = Foodorder
        fields = ["i_d","order_owner","name","price","quantity","picture",]

class User_details_serializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["email","Profile_picture"]