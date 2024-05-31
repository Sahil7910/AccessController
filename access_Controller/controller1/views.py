from django.shortcuts import render,redirect
from controller1.models import *
from django.contrib import messages
from django.contrib.auth.models import auth

import pandas as pd

import csv
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.




def index(request):
    return render (request,'index.html')





def organization(request):

    if request.method== 'POST':
        orgname=request.POST['orgname']
        orgid=request.POST['orgid']

        return render (request,'login.html')

    else:
            return render (request, 'org.html')





def login(request):

    if request.method == 'POST':
         username=request.POST['username']
         password=request.POST['password']
         user = auth.authenticate(username=username,password=password)

         if user is not None:
                auth.login(request,user)
                return redirect('home')
         else:
                messages.error(request,'invalid credentials...')
                return redirect('login')

    else:
         return render(request,'login.html')





def logout(request):
    auth.logout(request)
    return redirect('login')



def home(request):
    return render (request,'home.html')




def viewdoor(request):

    doors = Door.objects.all()

    return render (request,'viewdoors.html',{'doors':doors})




def adddoor(request):
    if request.method== 'POST':
        floor=request.POST['floor']
        name=request.POST['name']
        reader=request.POST['Reader']

        door= Door(floor=floor, name=name, reader= reader)
        door.save()
        messages.success(request, 'door added successfully...')
        print("floor:"+floor+ "name:"+name +"reader:"+ reader)
        return render (request,'addDoor.html')
    else:
         return render(request,'addDoor.html')
    


def addreader(request):
    
    if request.method == 'POST':
        model=request.POST['model']
        macid=request.POST['macid']
        doorlock=request.POST['doorlock']
        if Reader.objects.filter(macID=macid).exists():
             pass
        else:
             reader=Reader(model=model,macID=macid, doorlocked=doorlock)
             reader.save()
        return render (request,'addreader.html')
    else:
        return render(request,'addReader.html')






@api_view(['GET'])
def registerReader(request):
    macid = request.GET['mac']

    if Reader.objects.filter(macID=macid).exists():
        return Response("Reader Already Exists!!!", status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        mac= Reader(macID=mac)
        mac.save()
   
    return Response("successfully Register!!!", status=status.HTTP_201_CREATED)


    


def viewreader(request):

    reader= Reader.objects.all()

    return render (request,'viewReaders.html',{'reader':reader})








def adduser(request):
    dept = Department.objects.all()
    desg= Designation.objects.all()

    if request.method=='POST':
            name=request.POST['uname']
            cardid=request.POST['cardid']
            dep_id=request.POST['Department']
            desg_id=request.POST['Designation']

            department= Department.objects.get(pk=dep_id)
            designation= Designation.objects.get(pk=desg_id)
            adduser= User(name=name,cardid=cardid,designation=designation,department=department)
            adduser.save()
            return render (request,'addUser.html')
    else:
          return render (request,'addUser.html',{'dept':dept,'desg':desg})

def viewuser(request):

    users= User.objects.all()

    return render(request,'viewuser.html',{'users':users})




def addDepartment(request):
    if request.method == 'POST':
            department= request.POST['Department']

            dept= Department(department_name=department)
            dept.save()
            print(department)
            return render(request,'addDepartment.html')
    else:   
        return render(request,'addDepartment.html')
    

def viewDepartment(request):
    return render (request,'viewDepartment.html')




def addDesignation(request,):

    dept = Department.objects.all()

    if request.method == 'POST':
            designation= request.POST['designation']
            dept_id=request.POST['Department']

            department= Department.objects.get(pk=dept_id)

            add_designation= Designation(desg_name=designation, department= department)
            add_designation.save()
            return render(request,'addDesignation.html')
    else:
         return render(request,'addDesignation.html',{'dept':dept})
    



def viewDesignation(request):

    desg= Designation.objects.all()

    return render (request,'viewDesignation.html',{'desg':desg})


def importCard(request):

    if request.method=='POST':
        
        file = request.FILES['files']
        csv_reader= pd.read_csv(file)
        
        for index, row in csv_reader.iterrows():
             
             impcard= ImoprtCard(CardID=row['cardid'])
             impcard.save()
       
        return render(request,'importCard.html')
    else:
        return render(request,'importCard.html')
    



def viewCard(request):
    return render (request,'viewCard.html')