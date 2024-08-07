from django import forms

from fruitipediaApp.fruits.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryAddForm(CategoryForm):
    pass