from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cheese

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cheeses_index(request):
  cheeses = Cheese.objects.all()
  
  return render(request, 'cheeses/index.html', { 
    'cheeses': cheeses })

def cheeses_detail(request, cheese_id):
  cheese = Cheese.objects.get(id=cheese_id)
  return render(request, 'cheeses/detail.html', { 'cheese': cheese })

class CheeseCreate(CreateView):
  model = Cheese
  fields = '__all__'
  success_url = '/cheeses/'

class CheeseUpdate(UpdateView):
  model = Cheese
  fields = ['type', 'description', 'age']

class CheeseDelete(DeleteView):
  model = Cheese
  success_url = '/cheeses/'