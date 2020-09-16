from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('toys/', views.toys_index, name='index'),
   path('toys/<int:toy_id>/', views.toys_detail, name='detail'),
   path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
]