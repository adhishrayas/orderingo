from rest_framework import serializers
from .models import food

class Food_serializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = ["id","food_name","food_price"]