# Generated by Django 4.1.7 on 2023-03-08 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_booking', '0002_trip_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='station_photo',
        ),
    ]
