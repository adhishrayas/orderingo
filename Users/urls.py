from django.urls import path
from .views import get_cart_view,User_account_view,remove_from_cart,remove_object_from_cart


app_name = "Users"

urlpatterns = [
    path("",User_account_view.as_view(),name = "User details"),
    path("Mycart",get_cart_view.as_view(),name = "Get cart"),
    path("Mycart/<int:id>/remove_all",remove_object_from_cart,name = "Remove object"),
    path("Mycart/<int:id>/remove",remove_from_cart,name = "Decrease Quantity"),
    
]
