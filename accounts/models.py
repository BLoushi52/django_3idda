from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    dstrict = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    block = models.IntegerField()
    street = models.CharField(max_length=100)
    house = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.dstrict} - {self.area} - {self.block} - {self.street} - {self.house}"

