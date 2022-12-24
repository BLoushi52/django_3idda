from django.contrib import admin

from .models import Category, Item, Order, Review, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user")

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "category",)
    list_filter = ("title","user","category",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "item", "order_duration", "address", "price", "status")
    list_filter = ("user","item", "status", )

@admin.register(Favorite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ("id","user","item")
    list_filter = ("id","user","item")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "item", "rate", "review")
    list_filter = ("item","user",)
