from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = "date"

class TimeInput(forms.TimeInput):
    input_type = "time"

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "date", "time", "guests", "message"]
        widgets = {
            "date": DateInput(),
            "time": TimeInput(),
        }