from django.urls import path, include
from .views import HotelViewSet, RoomViewSet, BookingViewSet


urlpatterns = [
    path('hotels/', HotelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('hotel/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('rooms/', RoomViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]