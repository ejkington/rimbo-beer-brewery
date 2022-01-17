from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
BOOKED = ((0, "Pending"), (1, "Booked"), (2, "NotBooked"))
NUMBER_OF_GUESTS = ((0, "1"), (1, "2"), (2, "3"), (3, "4"), (4, "5"), (5, "6"))


class Event(models.Model):
    """
    Events model, slug is the identifyer, and featured image is the image thats uploaded to cloudinary and displayed in the view.
    """
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']


class Booked(models.Model):
    """
    Model for Booked, Choices is the number of guests with a maximim of 6 guests bookable at time
    """
    booking = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="booked")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    number_of_guests = models.IntegerField(choices=NUMBER_OF_GUESTS, default=1)
    approved = models.IntegerField(choices=BOOKED, default=0)
