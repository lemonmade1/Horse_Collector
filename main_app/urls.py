from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('horses/', views.horses_index, name='horses_index'),
  path('horses/<int:horse_id>/', views.horses_detail, name='horses_detail'),
]