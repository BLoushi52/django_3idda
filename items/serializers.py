from rest_framework import serializers
from items.models import Category, Favorite, Item, Order


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'user','title', "image"]

        

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField(source = 'category.title', read_only=True)
    class Meta:
        model = Item
        fields = ['id', 'title', "user", "category",'image', 'price', 'description']

class CreateItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Item
        fields = ['id', 'title', "user", "category",'image', 'price', 'description']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(read_only=True)
    item = ItemSerializer()
    class Meta:
        model = Order
        fields = ['id', "user", "item", 'order_duration', 'address','price', 'status', "start_date",  "end_date"]

class CreateOrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Order
        fields = ['id', "user", "item", 'order_duration', 'address','price', 'status', "start_date",  "end_date"]

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Favorite
        fields = ["id", "user", "item"]