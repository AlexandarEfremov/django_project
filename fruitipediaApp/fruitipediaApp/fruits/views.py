from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from fruitipediaApp.fruits.forms import CategoryAddForm, AddFruitForm, EditFruitForm
from fruitipediaApp.fruits.models import Fruit


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        "fruits": fruits
    }

    return render(request, 'common/dashboard.html', context)


class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


def edit_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    if request.method == "GET":
        form = EditFruitForm(instance=fruit)
    else:
        pass

    context = {
        "form": form
    }
    return render(request, 'fruits/edit-fruit.html')


def details_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    context = {
        "fruit": fruit
    }
    return render(request, 'fruits/details-fruit.html', context)


def delete_view(request, pk):
    return render(request, 'fruits/delete-fruit.html')


def create_category(request):
    if request.method == "GET":
        form = CategoryAddForm()
    else:
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        "form": form,
    }
    return render(request, 'categories/create-category.html', context)

