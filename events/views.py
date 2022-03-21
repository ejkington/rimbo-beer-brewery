from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Event, Booked
from .forms import BookingForm
from django.contrib.auth.models import User
from django.dispatch import receiver


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


class EditBookingView(TemplateView):
    """
    view for editing events booked by the user
    """
    template_name = 'edit_booking.html'
    
    def editbooking(self, request, slug):
        booking_form = BookingForm(data=request.POST)
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        event = get_object_or_404(booked=1)
        
        if booking_form.is_valid():
            booking_form.save()
        else:
            booking_form = BookingForm
        return render(
            request,
            "edit_booking.html",
            {
                "booking_form": BookingForm(),
                "user": user,
                "event": event,
            },
        )


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