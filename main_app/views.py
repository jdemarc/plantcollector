from django.shortcuts import render
from django.http import HttpResponse

# Simulating models...
class Toy:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, maker, description, release_year, value):
    self.name = name
    self.maker = maker
    self.description = description
    self.release_year = release_year
    self.value = value

toys = [
  Toy('Attack Armor Batman', 'Mattel', 'Batman superhero action figure', 2004, 400),
  Toy('Scratch the Cat', 'Playmates', 'TMNT minor character Scratch', 1993, 1500),
  Toy('Green Beret G.I. Joe', 'Hasbro', 'American hero toy G.I. Joe', 1966, 2100)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello.</h1>')

def about(request):
    return render(request, 'about.html')

def toys_index(request):
    return render(request, 'toys/index.html', {'toys' : toys})