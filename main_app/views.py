from django.shortcuts import render

from django.http import HttpResponse


class Cheese:  
  def __init__(self, name, type, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

cheeses = [
  Cheese('Parmigiano-Reggiano', 'hard', 'Italian hard, granular cheese produced from cow''s milk', 12),
  Cheese('Mozzarella', 'fresh', 'southern Italian cheese traditionally made from Italian buffalo''s milk by the pasta filata method', 0),
  Cheese('Camembert', 'soft white rind', 'a moist, soft, creamy, surface-ripened cow''s milk cheese', 1)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Cheesey!! :D</h1>')

def about(request):
  return render(request, 'about.html')

def cheeses_index(request):
  return render(request, 'cheeses/index.html', { 'cheeses': cheeses })