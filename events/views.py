from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event
from django.views.generic import TemplateView

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        booking = event.booked.filter(approved=True)
        
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking = booking_form.save(commit=False)
            booking.post = event
            booking.save()
        else:
            BookingForm = BookingForm()
        
        return render(
            request,
            'event-detail.html',
            {
                'event': event,
                'booking': booking,
                'booked': True,
                'bookingform': BookingForm()
            },
        )
          
    def event(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter.order_by('-created_on')
        event = get_object_or_404(queryset, slug=slug)
        
        return render(
            request,
            'event-detail.html',
            {
                'event': event
            },
        )

class OurBeersView(TemplateView):
    template_name = 'our-beers.html'