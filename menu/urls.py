from django.urls import path
from .views import Menu_items_view,Menu_item_detail_view


app_name = "menu"
urlpatterns = [
    path("",Menu_items_view.as_view(),name = "Menu items"),
    path("<int:pk>",Menu_item_detail_view.as_view(),name = "details"),
]
