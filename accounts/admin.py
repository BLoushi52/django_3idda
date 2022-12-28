from django.contrib import admin
from .models import Address


@admin.register(Address)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id" ,"user", "district", "area", "block", "street", "house")
    list_filter = ("user", "area")
