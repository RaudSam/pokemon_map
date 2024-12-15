from django.db import models  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200,
                                verbose_name='имя покемона на русском',
                                null=True)
    picture = models.ImageField(upload_to='poc_pictures/',
                                blank=True,
                                null=True)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                null=True)
    lat = models.FloatField(max_length=100)
    lon = models.FloatField(max_length=100)
    appear_at = models.DateTimeField(blank=True, default=timezone.now)
    disappear_at = models.DateTimeField(blank=True,
                                        null=True,
                                        default=None,
                                        verbose_name='Disappear at')
    level = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)
    strength = models.IntegerField(null=True, blank=True)
    defence = models.IntegerField(null=True, blank=True)
    stamina = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.pokemon.title_ru
