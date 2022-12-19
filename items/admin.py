from django.contrib import admin

from .models import Category, Item, Order, Review, Favorite

admin.site.register([Category, Item, Order, Review, Favorite])