from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plant, Insect
from .forms import WateringForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
def home(request):
  return render(request, 'about.html')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  insects_plant_doesnt_have = Insect.objects.exclude(id__in = plant.insects.all().values_list('id'))
  watering_form = WateringForm()
  return render(request, 'plants/detail.html', {
    'plant': plant, 'watering_form': watering_form,
    'insects': insects_plant_doesnt_have
  })

def add_watering(request, plant_id):
  form = WateringForm(request.POST)
  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.plant_id = plant_id
    new_watering.save()
  return redirect('detail', plant_id=plant_id)

def assoc_insect(request, plant_id, insect_id):
  Plant.objects.get(id=plant_id).insects.add(insect_id)
  return redirect('detail', plant_id=plant_id)

def unassoc_insect(request, plant_id, insect_id):
  Plant.objects.get(id=plant_id).insects.remove(insect_id)
  return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
  model = Plant
  fields = ['name', 'genus', 'species', 'description', 'age']
  success_url = '/plants/'

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['name', 'genus', 'species', 'description', 'age']
  # fields = ['name', 'description', 'age']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants/'

class InsectList(ListView):
  model = Insect

class InsectDetail(DetailView):
  model = Insect

class InsectCreate(CreateView):
  model = Insect
  fields = '__all__'

class InsectUpdate(UpdateView):
  model = Insect
  fields = ['name', 'color']

class InsectDelete(DeleteView):
  model = Insect
  success_url = '/insects/'