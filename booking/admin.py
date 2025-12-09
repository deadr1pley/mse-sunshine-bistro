from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "time", "guests", "status", "created_on")
    list_filter = ("status", "date")
    search_fields = ("name", "email")