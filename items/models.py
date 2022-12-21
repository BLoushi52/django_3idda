from django.contrib.auth.models import User
from django.db import models
from accounts.models import Address
from django.core.validators import MaxValueValidator, MinValueValidator



class Category(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.title}"

class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()

    

    def __str__(self):
        return f"{self.title}"
        

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="orders"
    )
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    order_duration = models.PositiveIntegerField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

class Review(models.Model):
    rate = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    review = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)






    