from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import Category, Favorite,Item, Order
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import  CategorySerializer, FavoriteSerializer, ItemSerializer, OrderSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsCreator
from items import models
from items.forms import CategoryForm, ItemForm
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class ItemView(ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        category_id = self.request.query_params.get("category_id", None)
        if category_id:
            return Item.objects.filter(category_id=category_id)
        return Item.objects.all()



    
class MyItemView(ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            return Item.objects.filter(user=self.request.user)
            

class ItemCreateView(CreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ItemDeleteView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsCreator]

class ItemUpdateView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsCreator]

class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyOrderView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            return Order.objects.filter(user=self.request.user)

class MyFavoriteView(ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            return Favorite.objects.filter(user=self.request.user)

class MyFavoriteCreateView(CreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyFavoriteDeleteView(DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'favorite_id'
    permission_classes = [IsCreator]

class IsFavoritedView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
            is_exists =  Favorite.objects.filter(user=self.request.user, item=item_id).exists()
            return JsonResponse({'is_exists': is_exists})





### HTML ###

@staff_member_required(login_url='login')
def home(request: HttpRequest):
    return render(request, "home.html")

@staff_member_required(login_url='login')
def get_items(request: HttpRequest):
    items: list[models.Item] = list(models.Item.objects.all())
    categories: list[models.Category] = list(models.Category.objects.all())
    context = {
        "items": items,
        "categories": categories,
    }
    return render(request, "items_list.html", context)


@staff_member_required(login_url='login')
def create_item(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect("items-list")

    context = {"form": form}
    return render(request, "item_create.html", context)


@staff_member_required(login_url='login')
def create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect("items-list")

    context = {"form": form}
    return render(request, "category_create.html", context)