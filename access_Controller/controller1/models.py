from django.db import models
from datetime import datetime    

# Create your models here.

class Door (models.Model):
    floor= models.CharField(max_length=20)
    name= models.CharField(max_length=50)
    reader=models.CharField(max_length=30,default='In Reader')
    lastaccess=models.DateTimeField(default=datetime.now())


class Reader(models.Model):
    model=models.CharField(max_length=50)
    macID=models.CharField(max_length=50)
    lastseen=models.DateTimeField()
    status=models.BooleanField()
    doorlocked=models.CharField(max_length=50)

class User (models.Model):
    name=models.CharField(max_length=50)
    cardid=models.CharField(max_length=50)
    status=models.BooleanField()

class Card(models.Model):
    cardid=models.CharField( max_length=50)
    import_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    deactivate_date=models.DateTimeField()
    username=models.CharField(max_length=50)
    status=models.BooleanField()