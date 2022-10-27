
from rest_framework import serializers

from .models import Room, Player

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'name', 'map_name', 'quantity', 'private', ]

class PlayerSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True, many=False)

    class Meta:
        model = Player
        fields = ['id', 'name', 'email', 'room',]
