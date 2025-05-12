# main_app/views.py

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cat

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# views.py
def cat_index(request):
    cats = Cat.objects.all()  # look familiar?
    return render(request, 'cats/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

def conclusion(request):
    return render(request, 'conclusion.html')

