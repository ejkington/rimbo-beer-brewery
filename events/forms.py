from django import forms
from .models import Booked


class BookingForm(forms.ModelForm):
    """
    Form rendering in the details and edit bookings page
    """
    class Meta:
        model = Booked
        fields = ('name', 'email', 'booking', 'number_of_guests', 'user')
        
