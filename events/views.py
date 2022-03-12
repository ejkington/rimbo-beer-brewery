from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Event, Booked
from .forms import BookingForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1)
    template_name = 'event.html'
    paginate_by = 6


class EventDetail(View):
    """
    Displays eventdetails page
    """
    def get(self, request, slug):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'event-detail.html',
            {
                'event': event,
                "isbooked": False,
                'booking_form': BookingForm()
            },
        )

    def post(self, request, slug):
        queryset = Event.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        event = get_object_or_404(queryset, slug=slug)
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            post.event = post
            booking_form.save()
        else:
            booking_form = BookingForm
        return render(
            request,
            "event-detail.html",
            {
                "post": post,
                "event": event,
                "isbooked": True,
                "booking_form": booking_form,
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