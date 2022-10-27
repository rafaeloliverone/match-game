from django.contrib import admin

from match.models import Room, Player
from .forms import PlayerForm


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'map_name', 'quantity', 'private',)
    list_filter = ('map_name', 'quantity',)
    ordering = ('name',)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'room')
    ordering = ('name',)
    form = PlayerForm


admin.site.register(Room, RoomAdmin)
admin.site.register(Player, PlayerAdmin)
