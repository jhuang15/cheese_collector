from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cheese
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  return render(request, 'cheeses/detail.html', {
    'cheese': cheese, 'feeding_form': feeding_form
  })

def add_feeding(request, cheese_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cheese_id = cheese_id
    new_feeding.save()
  return redirect('detail', cheese_id=cheese_id)

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