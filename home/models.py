from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=256)
    dep_description = models.TextField()