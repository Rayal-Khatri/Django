from django.db import models

class Features(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)

# Create your models here.
