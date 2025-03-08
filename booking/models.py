from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('executive', 'Executive Room'),
        ('executive_triple', 'Executive Triple Room'),
        ('executive_suite', 'Executive Suite'),
        ('deluxe_suite', 'Deluxe Suite'),
        ('presidential_suite', 'Presidential Suite'),
    ]
    
    name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=30, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='room_images/', blank=True, null=True)
    total_rooms = models.PositiveIntegerField(default=20)
    available_rooms = models.PositiveIntegerField(default=20)

    def __str__(self):
        return f"{self.name} (Available: {self.available_rooms}/{self.total_rooms})"

class Booking(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    services = models.TextField(blank=True, null=True)
    guest_name = models.CharField(max_length=255)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=50)
    card_holder = models.CharField(max_length=255)
    card_last4 = models.CharField(max_length=4)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.guest_name} for {self.room}"
