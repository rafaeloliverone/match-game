from django_filters import rest_framework as filters

from .models import Room


class RoomFilter(filters.FilterSet):
    map_name = filters.CharFilter(field_name='map_name')
    private = filters.BooleanFilter(field_name='private')

    class Meta:
        model = Room
        fields = ['map_name', 'private']
