from django.db import models
from datetime import datetime

class Features(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)

class Namesofpeople(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Age = models.IntegerField()
    

class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 10000)
    created = models.DateTimeField(default = datetime.now, blank=True ) 
