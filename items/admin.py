from django.contrib import admin

from .models import Category, Item

admin.site.register([Category, Item])