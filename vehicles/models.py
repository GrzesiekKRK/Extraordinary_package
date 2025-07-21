from django.db import models
from users.models import Department
import consts as vehicle_type

class Vehicle(models.Model):
    """
        The Vehicle model represents vehicles (Solo Truck, Tractor, Semi-trailer) operated by a specific company.
        It works in conjunction with the VehicleDimension component to improve overall performance.
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=vehicle_type)
    plates = models.CharField(max_length=20, unique=True)
    connected_to = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'type': 'Tractor'},
        related_name='attached_trailers'
    )

    def __str__(self):
        return f"{self.type} plates:{self.plates} "

class VehicleDimension(models.Model):
    """
    The VehicleDimension model represents cargo bed dimensions and payload capacity for each vehicle
    """
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name='dimensions')
    length = models.FloatField(help_text='length of the cargo bed in centimeters')
    width = models.FloatField(help_text='width  of the cargo bed in centimeters')
    height = models.FloatField(help_text='height of the cargo bed in centimeters')
    payload_capacity = models.FloatField(help_text='Gross Vehicle Weight in Kilograms', verbose_name='GVW')

    def __str__(self):
        return f"Cargo bed of {self.car.type} {self.car.plates}: Payload capacity:{self.payload_capacity}, Length:{self.length}, Width:{self.width}, Height:{self.height}"


