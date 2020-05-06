from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horse
from .forms import FeedingForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def horses_index(request):
  horses = Horse.objects.all()
  return render(request, 'horses/horses_index.html', { 
    'horses': horses, 
  })

def horse_detail(request, pk):
  horse = Horse.objects.get(id=pk)
  feeding_form = FeedingForm()
  return render(request, 'main_app/horse_detail.html', { 
    'horse': horse,
    'feeding_form': feeding_form 
  })

def add_feeding(request, pk):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.horse_id = pk
    new_feeding.save()
  return redirect('horses_detail', pk=pk)



class HorseList(ListView):
  model = Horse

  def get_queryset(self):
    return Horse.objects.all()

# class HorseDetail(DetailView):
#   model = Horse

class HorseCreate(CreateView):
  model = Horse
  fields = '__all__'  
  # fields = ['name', 'breed', 'description', 'age']

class HorseUpdate(UpdateView):
  model = Horse
  fields = ['breed', 'description', 'age']

class HorseDelete(DeleteView):
  model = Horse
  success_url = '/horses/'
