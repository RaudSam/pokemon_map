from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='poc_pictures/', blank=True)

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, blank=True)
    lat = models.FloatField(max_length=100)
    lon = models.FloatField(max_length=100)
