from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event, Booked


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'created_on')
    summernote_fields = ('description')


@admin.register(Booked)
class BookedAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'body')
    actions = ['approve_booking']
