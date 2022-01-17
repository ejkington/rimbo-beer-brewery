from django.test import TestCase
from .forms import Booked


class TestBookingform(TestCase):

    # test that message value needs to be provided
    def test_message_is_required(self):
        form = Bookingform({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    # test that message is named as an explicit field
    def test_fields_are_explicit_in_forms_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ('message',))