from .models import Booked
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booked
        fields = ('name', 'email', 'booking', 'number_of_guests',)