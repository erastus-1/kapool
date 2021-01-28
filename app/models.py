from location_field.models.plain import PlainLocationField
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from django.utils import timezone
from django.db import models
import datetime as dt
import cloudinary

# Create your models here.
class Driver(models.Model):

    name = models.OneToOneField(User,on_delete=models.CASCADE)
    bio =  HTMLField(blank=True)
    avatar = CloudinaryField('image', blank=True, null=True)
    vehicle = models.ForeignKey('app.Car', on_delete=models.CASCADE)
    pickup_location = models.ForeignKey('app.Place', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name



class Place(models.Model):
    city = models.ForeignKey('app.place', on_delete=models.CASCADE, max_length=255)
    location = models.ForeignKey('app.Driver', on_delete=models.CASCADE, max_length=255)

    
    def __str__(self):
        return self.place_city


class Car(models.Model):

    brand = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=20)


    def __str__(self):
        return self.car_brand

class Category(models.Model):

    pickup_location = models.CharField(max_length=20)
    arrival_destination = models.CharField(max_length=20)


    def __str__(self):
        return self.pickup_location