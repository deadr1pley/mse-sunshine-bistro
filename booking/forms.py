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
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "date": DateInput(attrs={"class": "form-control"}),
            "time": TimeInput(attrs={"class": "form-control"}),
            "guests": forms.NumberInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }