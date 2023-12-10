from django.urls import path
from . import views
urlpatterns=[
    path('', views.home,name='home'),
    path('dogs/', views.Adopt_Dogs,name='dogs'),
]