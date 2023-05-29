from django.contrib import admin
from .models import food,Foodorder,Cart
# Register your models here.
admin.site.register(food)
admin.site.register(Foodorder)
admin.site.register(Cart)