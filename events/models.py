from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
BOOKED = ((0, "Pending"), (1, "Booked"), (2, "NotBooked"))
CHOICES = ((0, "1"), (1, "2"), (2, "3"), (3, "4"), (4, "5"), (5, "6"))


class Event(models.Model):
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
   
    def __str__(self):
        return self.title
    
    
class Booked(models.Model):
    booking = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="booked")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    number_of_guests = models.IntegerField(choices=CHOICES, default=1)
    approved = models.IntegerField(choices=BOOKED, default=2)

    def __str__(self):
        return f"Comment {self.body} by {self.name}"