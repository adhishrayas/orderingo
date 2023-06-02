from django.urls import path
from .views import get_cart_view,User_account_view,Decrease_quantity,Delete_user,remove_object_from_cart,cost
from menu.views import Menu_item_detail_view


app_name = "Users"

urlpatterns = [
    path("",User_account_view.as_view(),name = "User details"),
    path("Delete_account",Delete_user.as_view(),name = "Delete User"),
    path("Mycart",get_cart_view.as_view(),name = "Get cart"),
    path("Mycart/cost",cost.as_view(),name = "Cost"),
    path("Mycart/<int:id>",Menu_item_detail_view.as_view(),name = "details"),
    path("Mycart/<int:id>/remove_all",remove_object_from_cart,name = "Remove object"),
    path("Mycart/<int:id>/remove",Decrease_quantity,name = "Decrease Quantity"),
    
]
