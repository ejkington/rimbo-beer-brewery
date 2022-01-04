from django.urls import path
from events import views
from .views import OurBeersView

urlpatterns = [
    path('events/', views.EventList.as_view(), name='events'),
    path('our-beers/', OurBeersView.as_view(), name='ourbeers'),
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event-detail'),
]
