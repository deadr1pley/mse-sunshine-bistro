from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Booking

# Create your views here.
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() #Save the booking in the database
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

def booking_edit(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect("booking_list")

    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        "booking/booking_edit.html",
        {"form": form, "booking": booking},
    )

def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        return redirect("booking_list")

    return render(
        request,
        "booking/booking_confirm_delete.html",
        {"booking": booking},
    )