from rest_framework import serializers
from .models import food,Foodorder

class Food_serializer(serializers.ModelSerializer):

    class Meta:
        model = food
        fields = ["id","food_name","food_price"]

class Food_detail_serializer(serializers.ModelSerializer):
      food_price = serializers.CharField(read_only = True)
      class Meta:
          model = food
          fields = ["id","food_name","food_price","serving_size"]

class get_cart_serializer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only = True)
    class Meta:
        model = Foodorder
        fields = ["i_d","name","price","quantity","total"]