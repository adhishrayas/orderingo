from rest_framework import serializers
from .models import food,Foodorder

class Food_serializer(serializers.ModelSerializer):

    class Meta:
        model = food
        fields = ["id","food_name","food_price","food_picture"]

class Food_detail_serializer(serializers.ModelSerializer):
      food_price = serializers.CharField(read_only = True)
      class Meta:
          model = food
          fields = ["id","food_name","food_price","serving_size"]

 