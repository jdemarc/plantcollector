from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Toy
from .forms import MaintainingForm

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
  maintaining_form = MaintainingForm()
  return render(request, 'toys/detail.html', {'toy': toy, 'maintaining_form': maintaining_form})

def add_maintenance(request, toy_id):
  form = MaintainingForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.toy_id = toy_id
    new_maintenance.save()
  return redirect('detail', toy_id=toy_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
  success_url = '/toys/'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'maker', 'description', 'release_year', 'value']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'