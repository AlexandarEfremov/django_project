from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from fruitipediaApp.fruits.forms import CategoryAddForm, AddFruitForm, EditFruitForm, DeleteFruitForm
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
        form = EditFruitForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        "form": form,
        "fruit": fruit
    }
    return render(request, 'fruits/edit-fruit.html', context)


def details_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    context = {
        "fruit": fruit
    }
    return render(request, 'fruits/details-fruit.html', context)


class DeleteFruitView(DeleteView):
    model = Fruit
    form_class = DeleteFruitForm
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')


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

