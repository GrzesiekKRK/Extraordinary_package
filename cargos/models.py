from django.db import models


class CargoTransport(models.Model):
    """
        The CargoTransport model represents customer cargo pickup and delivery point and price.
        Working in conjunction with OrderDimension for better performance
    """
    distance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Distance")
    price = models.DecimalField(max_digits=10, decimal_places=2, min_value=100)
    collection_date = models.DateTimeField(auto_now_add=True, verbose_name="Collection Date")
    collection_address = models.CharField(
        max_length=100,
        verbose_name="Collection Address",
        help_text="Collection address",
    )
    delivery_address = models.CharField(
        max_length=100,
        verbose_name="Delivery Address",
        help_text="Delivery address",
    )
    def __str__(self) -> str:
        return (f""
                f"Cargo {self.id}"
                f"Collection Date: {self.collection_date} "
                f"Collection address: {self.collection_address} "
                f"Delivery address: {self.delivery_address}"
                f"Distance: {self.distance}"
                f"Price: {self.price} "

                )

class CargoDimension(models.Model):
    """
    The CargoDimension model represents cargo dimensions it weights.
     With its help will decide what type of vehicle will do CargoTransport.
    """
    cargo = models.OneToOneField(CargoTransport, on_delete=models.CASCADE, related_name='dimensions')
    length = models.FloatField(help_text='length of the cargo bed in centimeters')
    width = models.FloatField(help_text='width  of the cargo bed in centimeters')
    height = models.FloatField(help_text='height of the cargo bed in centimeters')
    weight = models.FloatField(help_text='Gross Vehicle Weight in Kilograms', verbose_name='GVW')

    def __str__(self):
        return f"Cargo {self.cargo.id} : Weight:{self.weight}, Length:{self.length}, Width:{self.width}, Height:{self.height}"

