from django.urls import path
from .views import secret
app_name = "Payments"
urlpatterns = [
    path('',secret,name = "payments"),
]
