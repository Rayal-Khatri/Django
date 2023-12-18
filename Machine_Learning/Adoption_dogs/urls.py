from django.urls import path
from . import views
urlpatterns=[
    path('', views.home,name='home'),
    path('dogs/', views.Adopt_Dogs,name='dogs'),
    path('Shelthers/', views.Shelthers,name='Shelthers'),
    path('dogs/<str:dog_name>/', views.dog_image, name='dog_image'),
    path('Shelthers/<str:Shelther_name>', views.Shelther_image, name='Shelther_image'),
]