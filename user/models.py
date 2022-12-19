from django.db import models
from .forms import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    dob = models.DateTimeField()


