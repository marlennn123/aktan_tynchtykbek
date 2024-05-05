from django_filters import rest_framework as filters
from .models import Hotel, Room, Booking


class HotelFilters(filters.FilterSet):
    name = filters.ChoiceFilter(field_name='name', choices=Hotel.objects.all().values_list('name', 'name').distinct())
    country = filters.ChoiceFilter(field_name='country', choices=Hotel.objects.all().values_list('country', 'country').distinct())
    city = filters.ChoiceFilter(field_name='city', choices=Hotel.objects.all().values_list('city', 'city').distinct())
    address = filters.ChoiceFilter(field_name='address', choices=Hotel.objects.all().values_list('address', 'address').distinct())

    class Meta:
        model = Hotel
        fields = ['name', 'city', 'address', 'country']

class RoomFilters(filters.FilterSet):
    hotel = filters.ChoiceFilter(field_name='hotel', choices=Room.objects.all().values_list('hotel', 'hotel').distinct())
    min_room_number = filters.NumberFilter(field_name='room_number', lookup_expr='gte', label='Номер от')
    max_room_number = filters.NumberFilter(field_name='room_number', lookup_expr='lte', label='Номер до')
    min_capacity = filters.NumberFilter(field_name='capacity', lookup_expr='gte', label='Вместимость от')
    max_capacity = filters.NumberFilter(field_name='capacity', lookup_expr='lte', label='Вместимость до')
    min_price = filters.NumberFilter(field_name='price_per_night', lookup_expr='gte', label='Цена за ночь от')
    max_price = filters.NumberFilter(field_name='price_per_night', lookup_expr='lte', label='Цена за ночь до')

    class Meta:
        model = Room
        fields = ['hotel', 'min_room_number', 'max_room_number', 'min_capacity', 'max_capacity', 'min_price', 'max_price']

class BookingFilters(filters.FilterSet):
    STATUS_CHOICES = [
        ('not booked', 'Not Booked'),
        ('booked', 'Booked'),
        ('out of service', 'Out Of Service')
    ]
    status = filters.ChoiceFilter(field_name='status', choices=STATUS_CHOICES)
    class Meta:
        model = Booking
        fields = ['status']