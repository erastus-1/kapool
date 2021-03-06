# Generated by Django 3.1.5 on 2021-01-28 08:01

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=60)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('contact_info', models.CharField(max_length=50)),
                ('current_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='app.location')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver_profile', to=settings.AUTH_USER_MODEL)),
                ('pickup_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_pickup', to='app.location')),
            ],
        ),
    ]
