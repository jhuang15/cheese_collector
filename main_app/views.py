from django.shortcuts import render
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