from django.urls import path
from .views import add_to_cart,Menu_items_view,get_cart


app_name = "menu"
urlpatterns = [
    path("",Menu_items_view.as_view(),name = "Menu items"),
    path("<int:food_id>",add_to_cart,name = "Add to cart"),
    path("Mycart",get_cart,name = "My cart"),
]
