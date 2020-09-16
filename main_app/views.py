from django.shortcuts import render
from django.http import HttpResponse
from .models import Toy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello.</h1>')

def about(request):
  return render(request, 'about.html')

def toys_index(request):
  toys = Toy.objects.all()
  return render(request, 'toys/index.html', {'toys' : toys})

def toys_detail(request, toy_id):
  toy = Toy.objects.get(id=toy_id)
  return render(request, 'toys/detail.html', {'toy' : toy})

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
  success_url = '/toys/'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['description', 'value']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'