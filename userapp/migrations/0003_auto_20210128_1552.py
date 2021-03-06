# Generated by Django 3.1.5 on 2021-01-28 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210128_1552'),
        ('userapp', '0002_auto_20210128_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='current_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_location', to='app.location'),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='pickup_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rider_pickup', to='app.location'),
        ),
    ]
