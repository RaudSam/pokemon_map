from django.db import models  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='poc_pictures/',
                                blank=True,
                                null=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    lat = models.FloatField(max_length=100)
    lon = models.FloatField(max_length=100)
    appeared_at = models.DateTimeField(blank=True, default=timezone.now)
    disappeared_at = models.DateTimeField(blank=True,
                                          null=True,
                                          default=None,
                                          verbose_name='Disappeared at')
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)
