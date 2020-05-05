from django.shortcuts import render
from django.http import HttpResponse


class Horse:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

horses = [
  Horse('Lolo', 'tabby', 'foul little demon', 3),
  Horse('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Horse('Raven', 'black tripod', '3 legged horse', 4)
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def horses_index(request):
  return render(request, 'horses/index.html', { 
    'horses': horses, 
  })