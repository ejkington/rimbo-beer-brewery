from django import forms
from .models import Booked


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booked
        fields = ('name', 'email', 'booking', 'number_of_guests',)
