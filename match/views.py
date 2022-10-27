from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from .models import Room, Player
from .serializers import RoomSerializer, PlayerSerializer
from .filters import RoomFilter


class PlayerRoomCreateView(generics.GenericAPIView):
    serializer_class = PlayerSerializer
    
    def return_error_not_found(self):
        return Response(
            {
                'message': 'Nenhuma sala disponível no momento ou player não existe.',
                'status': status.HTTP_404_NOT_FOUND
            },
            status=status.HTTP_404_NOT_FOUND
        )

    def get_object(self):
        return Room.objects.filter(quantity__gt=0)

    def post(self, request, *args, **kwargs):
        room = self.get_object()
        player_id = kwargs.get('pk')

        try:
            instance = get_object_or_404(Player, id=player_id)
        except:
            return self.return_error_not_found()
            
        if room.exists():
            room_available = room.first()
            
            if (instance.room != room_available):
                instance.room = room_available
                instance.save()
                room_available.quantity -= 1
                room_available.save()

            return Response({'message': f'Player {instance.name} adicionado a sala {room_available.name}.', 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)

        return self.return_error_not_found()

class RoomViewSet(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_class = RoomFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]

class RoomSingleViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

class PlayersSingleViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayersViewSet(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
