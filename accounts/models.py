from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    block = models.PositiveIntegerField()
    street = models.CharField(max_length=100)
    house = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.id}: {self.district} - {self.area} - {self.block} - {self.street} - {self.house}"

