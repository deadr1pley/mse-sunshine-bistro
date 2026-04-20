from django.shortcuts import render
from .forms import BookingForm
from .models import Booking

# Create your views here.
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() #saving the booking in the data base

            return render(
                request,
                "booking/booking.html",
                {"form": BookingForm(), "success": True}
            )
    else:
        form = BookingForm()

    return render(
        request,
        "booking/booking.html",
        {"form": form}
    )

def booking_list(request):
    bookings = Booking.objects.all().order_by("-date", "-time")
    return render(
        request,
        "booking/booking_list.html",
        {"bookings": bookings},
    )