from django.urls import path
from .views import get_cart_view,User_account_view,Decrease_quantity,Delete_user,Object_remove_view


app_name = "Users"

urlpatterns = [
    path("",User_account_view.as_view(),name = "User details"),
    path("Delete_account",Delete_user.as_view(),name = "Delete User"),
    path("Mycart",get_cart_view.as_view(),name = "Get cart"),
    path("Mycart/<int:id>/remove_all",Object_remove_view.as_view(),name = "Remove object"),
    path("Mycart/<int:id>/remove",Decrease_quantity.as_view(),name = "Decrease Quantity"),
    
]
