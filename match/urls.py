from django.urls import path

from .views import PlayersViewSet, PlayersSingleViewSet, RoomViewSet, RoomSingleViewSet, PlayerRoomCreateView

urlpatterns = [
    path('players/', PlayersViewSet.as_view(), name='player_list_create'),
    path('player/<pk>', PlayersSingleViewSet.as_view(), name='player_single'),
    path('rooms/', RoomViewSet.as_view(), name='room_list_create'),
    path('room/<pk>', RoomSingleViewSet.as_view(), name='room_single'),
    path('search-room/<pk>', PlayerRoomCreateView.as_view(), name='room-available'),
]
