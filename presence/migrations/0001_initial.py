# Generated by Django 4.0.1 on 2022-04-16 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(help_text='Group channel name for this room', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(help_text='Reply channel for connection that is present', max_length=255)),
                ('last_seen', models.DateTimeField(default=django.utils.timezone.now)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presence.room')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('room', 'channel_name')},
            },
        ),
    ]
