from django.urls import path
from events import views
from .views import OurBeersView, EditBookingView

urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('our-beers/', OurBeersView.as_view(), name='our-beers'),
    path('', views.IndexView.as_view(), name='index'),
    path('edit/', EditBookingView.as_view(), name='edit_booking'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]
