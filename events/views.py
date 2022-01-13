from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Event
from .forms import BookingForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by("-created_on")
    template_name = 'event.html'
    paginate_by = 6


"""
Displays eventdetails page
"""


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        booking = event.booked.filter(approved=True)

        return render(
            request,
            'event-detail.html',
            {
                'event': event,
                "isbooked": False,
                'booking_form': BookingForm(),
            },
        )
    
    def event(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter.order_by('-created_on')
        event = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'event-detail.html',
            {
                'EventDetail': EventDetail,
                'booking_form': BookingForm(),
            },
        )

        def booked(self, request, slug, *args, **kwargs):
            queryset = Post.objects.filter(status=1)
            booked = get_object_or_404(queryset, slug=slug)
        
        
        booking_form = BookingForm(data=request.POST)
        
        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking = booking_form.save(commit=False)
            booking.post = booked
            booking.save()
        else:
            booking_form = BookingForm()
            
        return render(
            request,
            "event_detail.html",
            {
                "booked": booked,
                "isbooked": True,
                "booking_form": BookingForm()
            },
        )
    

"""
View for rendering our beers page
"""


class OurBeersView(TemplateView):
    template_name = 'our-beers.html'


"""
view for rendering index page
"""


class IndexView(TemplateView):
    template_name = 'index.html'
