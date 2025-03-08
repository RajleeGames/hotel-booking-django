from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('contact/', views.contact, name='contact'),
    path('accommodation/', views.accommodation, name='accommodation'),
    path('dine_wine/', views.dine_wine, name='dine_wine'),
    path('events_conferences/', views.events_conferences, name='events_conferences'),
    path('wellness_centre/', views.wellness_centre, name='wellness_centre'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
