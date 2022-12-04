from django.db import models

class Features(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)

class Namesofpeople(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Age = models.IntegerField(max_length=3)
    

