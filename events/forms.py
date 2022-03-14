from django import forms
from .models import Booked


class BookingForm(forms.ModelForm):
    """
    Form rendering in the details page
    """
    class Meta:
        model = Booked
        fields = ('name', 'email', 'booking', 'number_of_guests',)


class Editbooking(forms.ModelForm):
    """ 
    Form for editing users booking
    """
    class Meta:
        model = Booked
        fields = ('name', 'email', 'booking', 'number_of_guests',)
    