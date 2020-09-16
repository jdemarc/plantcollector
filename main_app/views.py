from django.shortcuts import render
from django.http import HttpResponse
from .models import Toy

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello.</h1>')

def about(request):
    return render(request, 'about.html')

def toys_index(request):
    toys = Toy.objects.all()
    return render(request, 'toys/index.html', {'toys' : toys})