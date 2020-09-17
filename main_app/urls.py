from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('plants/', views.plants_index, name='index'),
   path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
   path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
   path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
   path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
   path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
   path('plants/<int:plant_id>/assoc_insect/<int:insect_id>/', views.assoc_insect, name='assoc_insect'),
   path('plants/<int:plant_id>/unassoc_insect/<int:insect_id>/', views.unassoc_insect, name='unassoc_insect'),
   path('insects/', views.InsectList.as_view(), name='insects_index'),
   path('insects/<int:pk>/', views.InsectDetail.as_view(), name='insects_detail'),
   path('insects/create/', views.InsectCreate.as_view(), name='insects_create'),
   path('insects/<int:pk>/update/', views.InsectUpdate.as_view(), name='insects_update'),
   path('insects/<int:pk>/delete/', views.InsectDelete.as_view(), name='insects_delete'),
]