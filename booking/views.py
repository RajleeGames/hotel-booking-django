from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Room, Booking
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from decimal import Decimal
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- EMAIL SENDING FUNCTION USING GMAIL SMTP (HTML Email) ---
def send_gmail_oauth2(to_email, subject, plain_text_body, html_body):
    # Your Gmail credentials
    from_email = "hajraally499@gmail.com"
    app_password = "ngwu qlow quwl vlpr"
    
    # Create a multipart/alternative message
    msg = MIMEMultipart("alternative")
    # Use your hotel's name in the From header
    msg['From'] = "Kilimanjaro Magic Site Hotel <hajraally499@gmail.com>"
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach plain text and HTML parts
    part1 = MIMEText(plain_text_body, 'plain')
    part2 = MIMEText(html_body, 'html')
    msg.attach(part1)
    msg.attach(part2)
    
    try:
        # Connect to Gmail's SMTP server using SSL
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, app_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# --- VIEWS ---

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
            # Create booking instance
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

            # Prepare the email details
            subject = "Booking Confirmation - Kilimanjaro Magic Site Hotel"
            
            plain_text_body = f"""Dear {guest_name},

Thank you for booking with us at Kilimanjaro Magic Site Hotel. Here are your booking details:

Check-in Date: {checkin}
Check-out Date: {checkout}
Room Selected: {room}
Additional Services: {additional_services if additional_services else 'None'}
Total Cost: {total_cost}

We look forward to hosting you.

Best regards,
Kilimanjaro Magic Site Hotel
"""

            # Update the logo URL below with your actual domain if needed
            logo_url = "https://yourdomain.com/static/images/background.png"
            html_body = f"""
<html>
  <body style="font-family: Arial, sans-serif; line-height: 1.6;">
    <div style="text-align: center; margin-bottom: 20px;">
      <img src="{logo_url}" alt="Kilimanjaro Magic Site Hotel Logo" style="max-width:200px;">
    </div>
    <h2 style="color:#007bff; text-align: center;">Booking Confirmation</h2>
    <p>Dear {guest_name},</p>
    <p>Thank you for booking with us at <strong>Kilimanjaro Magic Site Hotel</strong>. Here are your booking details:</p>
    <ul>
      <li><strong>Check-in Date:</strong> {checkin}</li>
      <li><strong>Check-out Date:</strong> {checkout}</li>
      <li><strong>Room Selected:</strong> {room}</li>
      <li><strong>Additional Services:</strong> {additional_services if additional_services else 'None'}</li>
      <li><strong>Total Cost:</strong> {total_cost}</li>
    </ul>
    <p>We look forward to hosting you.</p>
    <p>Best regards,<br/>
       Kilimanjaro Magic Site Hotel</p>
  </body>
</html>
"""

            # Send confirmation email to the guest using HTML email
            send_gmail_oauth2(guest_email, subject, plain_text_body, html_body)
            return redirect('booking_success')

        except Exception as e:
            print(f"Error creating booking: {e}")
            return HttpResponse(f"Error creating booking: {e}")

    return render(request, 'booking/book_room.html', {'room': room})

def booking_success(request):
    return render(request, 'booking/booking_success.html')

# This view is provided if you need to test email sending separately.
def send_booking_confirmation(request):
    to_email = "ikramally499@gmail.com"
    subject = "Booking Confirmation - Kilimanjaro Magic Site Hotel"
    plain_text_body = "Your booking has been confirmed."
    html_body = """
    <html>
      <body>
        <h2>Booking Confirmation</h2>
        <p>Your booking has been confirmed.</p>
      </body>
    </html>
    """
    send_gmail_oauth2(to_email, subject, plain_text_body, html_body)
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
