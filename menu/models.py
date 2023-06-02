from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from Users.models import CustomUser
# Create your models here.
SERVING_SIZE = [
    ("L","Large"),
    ("S","Small"),
    ("M","Medium"),
    ("F","Full"),
    ("H","Half"),
]
class food(models.Model):
    food_name = models.CharField("Dish name",max_length=255,blank=False)
    serving_size = models.CharField(choices=SERVING_SIZE,default="L",max_length=255)
    food_price = models.IntegerField("Dish price",blank=False)
    final_output_price = models.IntegerField("Dish Output price",blank=True,null=True)
    food_picture = models.ImageField("Dish Image",blank=True,null=True,upload_to='Menu_items/')
    food_rating = models.IntegerField(default=0)

    def __str__(self):
        return str(self.food_name)
        
class Cart(models.Model):
    Site_user = models.ForeignKey(CustomUser,on_delete= models.CASCADE,null=True)
    order_date = models.DateTimeField(blank=True,null = True)
    cart_total = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return str(self.Site_user) 
        
class Foodorder(models.Model):
    order_owner = models.CharField(blank=False,max_length=255,default="")
    i_d = models.IntegerField(blank=False)
    cart_used = models.ManyToManyField(Cart)
    name = models.TextField("Order item name",blank=False,max_length=255)
    price = models.IntegerField("Order item price",blank = False)
    quantity = models.IntegerField("Order item quantity",blank=False,default=0)
    picture = models.ImageField("Order item picture",blank=True,null = True)

    def __str__(self):
        return str(self.name) 
    
    def cost(self):
        return int(self.quantity*self.price)

    