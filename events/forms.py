from django import forms
from .models import Booked


class BookingForm(forms.ModelForm):
    """
    Form rendering in the details page
    """
    class Meta:
        model = Booked
        fields = ('name', 'email', 'number_of_guests',)