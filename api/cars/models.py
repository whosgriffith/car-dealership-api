from decimal import Decimal

from django.db import models
from django.core.validators import RegexValidator, MinValueValidator


class VEHICLE_TYPE(models.IntegerChoices):
    PICKUP = 0, "Autos"
    HATCHBACK = 1, "Pickups y Comerciales"
    SEDAN = 2, "SUVs y Crossovers"


class Car(models.Model):
    make = models.CharField(max_length=30)
    model_name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    model_year = models.IntegerField(
        validators=[RegexValidator(r'^\d{4}$')]  # Numbers of 4 digits
    )
    price = models.DecimalField(
        decimal_places=0,
        max_digits=10,
        validators=[MinValueValidator(Decimal('0'))],
        blank=True,
        null=True
    )
    type = models.IntegerField(choices=VEHICLE_TYPE, null=True, blank=True)
    images = models.ManyToManyField('CarImage', related_name='cars')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    features = models.ManyToManyField(
        'CarFeature',
        related_name='cars',
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['make', 'model_name', 'model_year'],
                name='unique_car_constraint'
            )
        ]

    def __str__(self):
        return f"{self.make} - {self.model_name} ({self.model_year})"


class CarImage(models.Model):
    file = models.ImageField()
    image_description = models.CharField(max_length=30)

    def __str__(self):
        return self.image_description


class CarFeature(models.Model):
    image = models.ForeignKey(CarImage, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
