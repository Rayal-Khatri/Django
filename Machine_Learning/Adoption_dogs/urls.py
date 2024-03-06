from django.urls import path
from . import views
urlpatterns=[
    path('', views.home,name='home'),
    path('dogs/', views.Adopt_Dogs,name='dogs'),
    path('Shelters/', views.Shelters,name='Shelters'),
    path('dogs/<str:dog_name>/', views.dog_image, name='dog_image'),
    path('Shelters/<str:Shelter_name>', views.Shelter_image, name='Shelter_image'),
]