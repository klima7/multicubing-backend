# Generated by Django 4.0.1 on 2022-04-19 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_last_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='last_activity',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
