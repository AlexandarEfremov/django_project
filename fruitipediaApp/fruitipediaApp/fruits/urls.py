from django.urls import path

from fruitipediaApp.fruits import views

urlpatterns = [
    path('', views.index, name='index'),
]