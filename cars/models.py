import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey

# Create your models here.

REGION_CHOICES = [
    ("JDM", "Japanese"),
    ("GER", "German"),
    ("USA", "American Muscle"),
    ("KOR", "Korean"),
    ("ITA", "Italian"),
    ("FRA", "French"),
    ("UK", "British"),
    ("OTH", "Other"),
]

def upload_to_car(instance, filename):
    return f'cars/{instance.owner.username}/{filename}'

def upload_to_mod(instance, filename):
    return f'mods/{instance.car.owner.username}/{instance.car.id}/{filename}'

class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_to_car, null=True, blank=True)
    year = models.PositiveIntegerField()
    region = models.CharField(max_length= 3,choices = REGION_CHOICES)
    models.ImageField(upload_to=upload_to_car)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/cars/{self.id}/'

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Modification(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='modifications')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to=upload_to_mod, null=True, blank=True)
    date_installed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} on {self.car}'