# Generated by Django 3.2 on 2024-12-15 12:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='имя покемона на русском')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='poc_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(max_length=100)),
                ('lon', models.FloatField(max_length=100)),
                ('appear_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('disappear_at', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Disappear at')),
                ('level', models.IntegerField(blank=True, null=True)),
                ('health', models.IntegerField(blank=True, null=True)),
                ('strength', models.IntegerField(blank=True, null=True)),
                ('defence', models.IntegerField(blank=True, null=True)),
                ('stamina', models.IntegerField(blank=True, null=True)),
                ('pokemon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
