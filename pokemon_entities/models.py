from django.db import models  # noqa F401
from django.utils import timezone


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200,
                                verbose_name='имя покемона на русском',
                                null=True)
    title_en = models.CharField(null=True,
                                blank=True,
                                max_length=200,
                                verbose_name='имя покемона на английском')
    title_jp = models.CharField(null=True,
                                blank=True,
                                max_length=200,
                                verbose_name='имя покемона на японском')
    picture = models.ImageField(upload_to='poc_pictures/',
                                blank=True,
                                null=True,
                                verbose_name="изображение")
    description = models.TextField(null=True,
                                   blank=True,
                                   verbose_name="описание")
    previous_evolution = models.ForeignKey('self',
                                           on_delete=models.CASCADE,
                                           null=True, blank=True,
                                           related_name='next_evolutions',
                                           verbose_name='предыдущая эволюция покемона')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE,
                                null=True,
                                verbose_name='покемон')
    lat = models.FloatField(max_length=100,
                            verbose_name='широта')
    lon = models.FloatField(max_length=100,
                            verbose_name='долгота')
    appear_at = models.DateTimeField(blank=True, default=timezone.now,
                                     verbose_name='дата и время появления')
    disappear_at = models.DateTimeField(blank=True,
                                        null=True,
                                        default=None,
                                        verbose_name='дата и время исчезновения')
    level = models.IntegerField(null=True, blank=True,
                                verbose_name='уровень')
    health = models.IntegerField(null=True, blank=True,
                                 verbose_name='здоровье')
    strength = models.IntegerField(null=True, blank=True,
                                   verbose_name='сила')
    defence = models.IntegerField(null=True, blank=True,
                                  verbose_name='защита')
    stamina = models.IntegerField(null=True, blank=True,
                                  verbose_name='выносливость')

    def __str__(self):
        return self.pokemon.title_ru
