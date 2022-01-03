from django.urls import path
from tourbooking import views

urlpatterns = [
    path('event/', views.EventList.as_view(), name='event'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event-detail'),
    path('index/', views.index.as_view(), name='index'),
    path('ourbeers/', views.ourbeers.as_view(), name='our-beers'),
]