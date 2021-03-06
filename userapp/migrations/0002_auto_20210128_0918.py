# Generated by Django 3.1.5 on 2021-01-28 09:18

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210128_0918'),
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='bio',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='current_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='app.place'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='pickup_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_pickup', to='app.place'),
        ),
    ]
