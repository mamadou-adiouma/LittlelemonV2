from django.forms import ModelForm
from django import forms
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    reservation_date = forms.DateField(input_formats=["%Y-%m-%d", "%d/%m/%Y"])

    class Meta:
        model = Booking
        fields = "__all__"
