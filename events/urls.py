from django.urls import path
from events import views

urlpatterns = [
    path('', views.EventList.as_view(), name='index'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event-detail'),
]