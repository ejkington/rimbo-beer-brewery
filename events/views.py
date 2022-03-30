from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .models import Event, Booked
from .forms import BookingForm


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
            if request.user.is_authenticated:
                user = request.user
            form = BookingForm(user)
            booking_form.save()
        else:
            booking_form = BookingForm
        return render(
            request,
            "event_detail.html",
            {
                "post": post,
                "user": user,
                "event": event,
                "isbooked": True,
                "form": form,
                "booking_form": booking_form,
            },
        )


class BookingList(ListView):
    """
    displays all booked events by user
    """
    template_name = 'edit_booking.html'

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        booked_events = Booked.objects.filter(user=user)
        return render(
            request,
            self.template_name,
            {
                'booked_events': booked_events,
                'user': user,
            })


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
