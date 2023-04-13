# Generated by Django 4.2 on 2023-04-13 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='security_allocation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='route',
            name='van_number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]