
from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=30,default="")
    email=models.EmailField(max_length=50,default="")
    address=models.CharField(max_length=200,default="")
    suggestions=models.TextField(max_length=200,default="")

def __str__(self):
    return self.name