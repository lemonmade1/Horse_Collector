from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horse


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def horses_index(request):
#   horses = Horse.objects.all()
#   return render(request, 'horses/index.html', { 
#     'horses': horses, 
#   })

# def horses_detail(request, horse_id):
#   horse = Horse.objects.get(id=horse_id)
#   return render(request, 'horses/detail.html', { 
#     'horse': horse 
#   })

class HorseList(ListView):
  model = Horse

  def get_queryset(self):
    return Horse.objects.all()

class HorseDetail(DetailView):
  model = Horse

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
