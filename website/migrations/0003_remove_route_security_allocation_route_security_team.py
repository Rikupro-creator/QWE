# Generated by Django 4.2 on 2023-04-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_route_security_allocation_route_van_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='security_allocation',
        ),
        migrations.AddField(
            model_name='route',
            name='security_team',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
    ]