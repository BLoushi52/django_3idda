from django import forms
from .models import Category, Item


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title", "image"]

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["category", "title", "image","description","price","image"]




        
        
 