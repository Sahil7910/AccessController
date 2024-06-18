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
    status=models.BooleanField(default=True)
    doorlocked=models.CharField(max_length=50)

class Card(models.Model):
    cardid=models.CharField( max_length=50)
    import_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    deactivate_date=models.DateTimeField()
    username=models.CharField(max_length=50)
    status=models.BooleanField()

    def __str__(self):
        return self.cardid

class Department(models.Model):
    department_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.department_name 

class Designation(models.Model):
    desg_name=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.desg_name 


class User (models.Model):
    name=models.CharField(max_length=50)
    card_id=models.ForeignKey(Card,on_delete=models.CASCADE)
    student_id=models.CharField(max_length=50)
    status=models.IntegerField(max_length=3,default=0)


    # status=models.BooleanField(default=True)
    # designation= models.ForeignKey( Designation,on_delete=models.CASCADE)
    # department= models.ForeignKey(Department, on_delete=models.CASCADE)
        
    # def __str__(self):
    #     return self.designation+" "+self.department or ''

class ImoprtCard(models.Model):
    CardID = models.CharField(max_length=50) 


class register(models.Model):
 mac=models.IntegerField()

class Checkin(models.Model):
    cardid=models.CharField(max_length=250)
    macID=models.CharField(max_length=250)
    datetime=models.DateTimeField(default=datetime.now())
    