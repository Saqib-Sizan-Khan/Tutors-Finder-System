from django.db import models

# Create your models here.

class Subjects(models.Model):
    subject_Name = models.CharField(max_length=20)
    subject_ID = models.IntegerField(primary_key=True)

class location(models.Model):
    location_Name = models.CharField(max_length=20)
    location_ID = models.IntegerField(primary_key=True)