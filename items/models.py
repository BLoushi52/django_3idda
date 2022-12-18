from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")

    def __str__(self):
        return f"{self.id}: {self.user.username} : {self.title}"

class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories"
    )
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f"{self.id}: {self.user.username} : {self.title}, {self.category.title}"
        