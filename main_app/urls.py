from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('horses/', views.horses_index, name='horses_index'),
  path('horses/<int:pk>/', views.horse_detail, name='horses_detail'),
  path('horses/create/', views.HorseCreate.as_view(), name='horses_create'),
  path('horses/<int:pk>/update/', views.HorseUpdate.as_view(), name='horses_update'),
  path('horses/<int:pk>/delete/', views.HorseDelete.as_view(), name='horses_delete'),  
  path('horses/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),

]
