from django.db import models

# Create your models here.

class Request(models.Model):
    educatorType = models.CharField(max_length=20)
    educatorId = models.IntegerField()
    educatorName = models.CharField(max_length=30)
    parentId = models.IntegerField()
    parentName = models.CharField(max_length=30)

class Deals(models.Model):
    educatorType = models.CharField(max_length=20)
    educatorId = models.IntegerField()
    educatorName = models.CharField(max_length=30)
    parentId = models.IntegerField()
    parentName = models.CharField(max_length=30)


