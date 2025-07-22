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
    """
        The Department model represents office or transport hub for company
    """
    type = models.CharField(max_length=100, choices=departments)
    address = models.CharField(max_length=100, unique=True, verbose_name="Building Address")

    def __str__(self) -> str:
        return f"{self.type} {self.address}"


class Employee(CustomUser):
    """
        The Employee model creates info about drivers assigned to transport departments or office employees.
    """
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    driver = models.BooleanField(default=True)
    driver_semi = models.BooleanField(default=False)
    on_route = models.BooleanField(default=False)

    def __str__(self) -> str:
        return (f""
                f"{self.custom_user.first_name} {self.custom_user.last_name}"
                f" department {self.department.type} address {self.department.address}"
                )
