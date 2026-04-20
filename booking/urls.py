from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking, name="booking"),
    path("list/", views.booking_list, name="booking_list"),
]