# Generated by Django 4.2 on 2023-04-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routeID', models.PositiveIntegerField()),
                ('starting_location', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('distance', models.FloatField()),
                ('estimated_arrival_time', models.TimeField()),
                ('actual_arrival_time', models.TimeField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
