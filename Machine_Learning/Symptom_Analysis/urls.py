from django.urls import path
from . import views
urlpatterns=[
    path('', views.home,name='home'),
    path('Predict/', views.predict_api,name='predict_api'),
]