from django.contrib.auth.models import AbstractUser
from django.db import models
import consts as departments

class CustomUser(AbstractUser):
    """
        Custom user model extending the base AbstractUser to include additional fields
        specific to the application. This includes role management, user-specific
        information, and secondary contact details.
    """
    email = models.EmailField(max_length=50,unique=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True)
    secondary_email = models.EmailField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Secondary Email",
        help_text="Emergency email if primary email is lost. Optional",
    )
    address = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Billing Address",
        help_text="Billing address",
    )
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Department(models.Model):
    type = models.CharField(max_length=100, choices=departments)
    address = models.CharField(max_length=100, unique=True, verbose_name="Building Address")

    def __str__(self) -> str:
        return f"{self.type} {self.address}"

class EMPLOYEE(CustomUser):
    """
        The Employee model creates info about drivers assigned to transport departments
    """
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    driver = models.BooleanField(default=True)
    driver_semi = models.BooleanField(default=False)

