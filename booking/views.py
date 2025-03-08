from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Room, Booking
from .email_utils import send_gmail_oauth2  # Ensure this exists in your project
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from decimal import Decimal

def home(request):
    rooms = Room.objects.all()
    return render(request, 'booking/home.html', {'rooms': rooms})



def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        additional_services = ", ".join(request.POST.getlist('services'))
        guest_name = request.POST.get('guest_name')
        guest_email = request.POST.get('guest_email')
        guest_phone = request.POST.get('guest_phone')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        total_cost = request.POST.get('total_cost')

        # Convert total_cost to Decimal
        try:
            total_cost = Decimal(total_cost) if total_cost else Decimal(0)
        except Exception as e:
            print(f"Error converting total_cost: {e}")
            total_cost = Decimal(0)

        card_last4 = card_number[-4:] if card_number and len(card_number) >= 4 else ''

        print(f"Booking details: {guest_name}, {guest_email}, {checkin}, {checkout}, {total_cost}")

        try:
            booking = Booking.objects.create(
                check_in=checkin,
                check_out=checkout,
                room=room,
                services=additional_services,
                guest_name=guest_name,
                guest_email=guest_email,
                guest_phone=guest_phone,
                card_holder=card_name,
                card_last4=card_last4,
                total_cost=total_cost,
            )
            messages.success(request, "Booking Confirmed!")
            return redirect('booking_success')

        except Exception as e:
            print(f"Error creating booking: {e}")
            return HttpResponse(f"Error creating booking: {e}")

    return render(request, 'booking/book_room.html', {'room': room})


def booking_success(request):
    return render(request, 'booking/booking_success.html')

def send_booking_confirmation(request):
    to_email = "ikramally499@gmail.com"
    subject = "Booking Confirmation"
    body = "Your booking has been confirmed."
    send_gmail_oauth2(to_email, subject, body)
    return HttpResponse("Email sent!")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def contact(request):
    return render(request, 'booking/contact.html')

def accommodation(request):
    return render(request, 'booking/accommodation.html')

def dine_wine(request):
    return render(request, 'booking/dine_wine.html')

def events_conferences(request):
    return render(request, 'booking/events_conferences.html')

def wellness_centre(request):
    return render(request, 'booking/wellness_centre.html')

def upcoming_events(request):
    return render(request, 'booking/upcoming_events.html')
