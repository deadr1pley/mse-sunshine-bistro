from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking, name="booking"),
    path("list/", views.booking_list, name="booking_list"),
    path("edit/<int:booking_id>/", views.booking_edit, name="booking_edit"),
    path("delete/<int:booking_id>/", views.booking_delete, name="booking_delete"),
]