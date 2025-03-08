from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'room', 'guest_name', 'guest_email', 'guest_phone',
            'check_in', 'check_out', 'services', 'card_last4'
        ]
