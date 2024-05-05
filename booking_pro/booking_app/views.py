from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .serializers import HotelSerializer, RoomSerializer, BookingSerializer
from .filters import HotelFilters, RoomFilters, BookingFilters
from .models import Hotel, Room, Booking


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', ]
    filterset_class = HotelFilters

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['hotel', ]
    filterset_class = RoomFilters

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = BookingFilters
