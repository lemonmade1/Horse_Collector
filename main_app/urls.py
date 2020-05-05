from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('horses/', views.horses_index, name='index'),
  path('horses/<int:horse_id>/', views.horses_detail, name='detail'),
  path('horses/create/', views.HorseCreate.as_view(), name='horses_create'),
  path('horses/<int:pk>/update/', views.HorseUpdate.as_view(), name='horses_update'),
  path('horses/<int:pk>/delete/', views.HorseDelete.as_view(), name='horses_delete'),
]