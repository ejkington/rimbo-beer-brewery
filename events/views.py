from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import Event, Booked
from .forms import BookingForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class EventList(generic.ListView):
    """
    displays all events
    """
    model = Event
    queryset = Event.objects.filter(status=1)
    template_name = 'event.html'
    paginate_by = 6


class EventDetail(View):
    """
    Displays event details page
    """
    def get(self, request, slug):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'event_detail.html',
            {
                'event': event,
                "isbooked": False,
                'booking_form': BookingForm()
            },
        )

    def post(self, request, slug):
        post = get_object_or_404(Event, slug=slug)
        event = get_object_or_404(Event, slug=slug)
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            post.event = post
            booking_form.save()
        else:
            booking_form = BookingForm
        return render(
            request,
            "event_detail.html",
            {
                "post": post,
                "event": event,
                "isbooked": True,
                "booking_form": booking_form,
            },
        )


class BookingList(ListView):
    """
    displays all booked events by user
    """
    model = Event
    queryset = Event.objects.filter(status=1)
    template_name = 'edit_booking.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        Bookings = Event.objects.filter(slug=self.kwargs.get('slug'))

        return context

class OurBeersView(TemplateView):
    """
    View for rendering our beers page
    """
    template_name = 'our-beers.html'


class IndexView(TemplateView):
    """
    view for rendering index page
    """
    template_name = 'index.html'
