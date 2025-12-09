from django.shortcuts import render
from .forms import BookingForm

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
