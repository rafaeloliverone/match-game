import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .utils.models import MAP_CHOICES


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Room(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Nome', max_length=100, null=False, blank=False)
    map_name = models.CharField(
        'Mapa',
        max_length=255,
        null=False,
        blank=False,
        choices=MAP_CHOICES
    )
    quantity = models.IntegerField(
        'Quantidade',
        null=False,
        blank=False,
        default=2,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(2)
        ]
    )
    private = models.BooleanField(
        'Privada', blank=False, null=False, default=False)

    def __str__(self):
        return self.name


class Player(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Nome', max_length=100, null=False, blank=False)
    email = models.EmailField('E-mail', unique=True, null=False, blank=False)
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        verbose_name='Sala',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.name} - {self.room}'
