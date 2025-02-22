from django.shortcuts import render
from .models import Animal

def home(request):
    animal_objects = Animal.objects.all()
    context = {'animals':animal_objects}
    return render(request, "home.html", context=context)

def animal_info(request, pk):
    animal_objects = Animal.objects.get(id=pk)
    context = {'animal':animal_objects}

    return render(request, "animal.html" ,context=context)