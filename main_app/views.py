from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Horse, Toy
from .forms import FeedingForm

# Create your views here.
def signup(request):
  error_message = ''
  
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'

  form = UserCreationForm()
  context = {
    'form': form, 
    'error_message': error_message
    }
  return render(request, 'registration/signup.html', context)

# HOME AND ABOUT PAGES
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# CRUD FEATURES
class HorseCreate(LoginRequiredMixin, CreateView):
  model = Horse
  fields = ['name', 'breed', 'description', 'age']
  # fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class HorseUpdate(LoginRequiredMixin, UpdateView):
  model = Horse
  fields = ['name', 'breed', 'description', 'age']

class HorseDelete(LoginRequiredMixin, DeleteView):
  model = Horse
  success_url = '/horses/'


@login_required
def horses_index(request):
  horses = Horse.objects.filter(user = request.user)
  return render(request, 'horses/index.html', { 'horses': horses })

@login_required
def horses_detail(request, horse_id):
  horse = Horse.objects.get(id=horse_id)
  toys_horse_doesnt_have = Toy.objects.exclude(id__in = horse.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'horses/detail.html', { 
    'horse': horse,
    'feeding_form': feeding_form,
    'toys': toys_horse_doesnt_have,
  })

@login_required
def add_feeding(request, horse_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.horse_id = horse_id
    new_feeding.save()
  return redirect('detail', horse_id=horse_id)

# TOYS (many to many relationship)
@login_required
def assoc_toy(request, horse_id, toy_id):
  Horse.objects.get(id=horse_id).toys.add(toy_id)
  return redirect('detail', horse_id=horse_id)

@login_required
def unassoc_toy(request, horse_id, toy_id):
  Horse.objects.get(id=horse_id).toys.remove(toy_id)
  return redirect('detail', horse_id=horse_id) 

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'


  # class HorseList(LoginRequiredMixin, ListView):
#   model = Horse

#   def get_queryset(self):
#     return Horse.objects.filter(user=self.request.user)