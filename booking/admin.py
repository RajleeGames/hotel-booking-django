from django.contrib import admin
from .models import Room, Booking


admin.site.site_header = "Kilimanjaro Magic Site Hotel Admin Site"
admin.site.site_title = "Kilimanjaro Magic Site Hotel Admin Portal"
admin.site.index_title = "Welcome to Kilimanjaro Magic Site Hotel Admin"

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'price_per_night', 'available_rooms', 'total_rooms')
    list_filter = ('room_type',)
    search_fields = ('name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'room', 'check_in', 'check_out', 'total_cost', 'created_at')
    search_fields = ('guest_name', 'guest_email', 'room')
    list_filter = ('check_in', 'check_out')
