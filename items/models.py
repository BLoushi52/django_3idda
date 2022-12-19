from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.title}"

class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="Itemes"
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    rating = models.FloatField(null=True)

    def __str__(self):
        return f"{self.id}: {self.user.username} : {self.title}, {self.category.title}"
        
class Address(models.Model):
    dstrict = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    block = models.IntegerField()
    street = models.CharField(max_length=100)
    house = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="orderes"
    )
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    order_duration = models.FloatField()
    address = models.ForeignKey(Address, on_delete=models.PROTECT)

class Review(models.Model):
    rate = models.FloatField()
    review = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)






    