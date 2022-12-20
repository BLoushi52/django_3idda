
from django.http import HttpRequest
from django.shortcuts import redirect, render

from .models import Category,Item
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import  CategorySerializer, ItemSerializer, ItemUpdateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsCreator
from items import models
from items.forms import CategoryForm, ItemForm
from django.contrib.admin.views.decorators import staff_member_required


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class ItemView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
    
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
    serializer_class = ItemUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsCreator]




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