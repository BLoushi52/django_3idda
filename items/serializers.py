from rest_framework import serializers
from items.models import Category, Item, Order


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'user','title', "image"]

        

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Item
        fields = ['id', 'title', "user", "category",'image', 'price', 'description']


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title','image', 'category','description','price']

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = ['id', "user", "item", 'order_duration', 'address','price', 'status']
