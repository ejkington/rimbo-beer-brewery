from django.urls import path
from events import views
from .views import OurBeersView

urlpatterns = [
    path('our-beers/', OurBeersView.as_view(), name='ourbeers'),
    path('', views.EventList.as_view(), name='index'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event-detail'),
]