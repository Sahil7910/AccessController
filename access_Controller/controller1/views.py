from tabnanny import check
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import auth
from datetime import datetime,date,timedelta


import pandas as pd

import csv
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


def index(request):
    return render(request, 'index.html')


def organization(request):
    if request.method == 'POST':
        orgname = request.POST['orgname']
        orgid = request.POST['orgid']

        return render(request, 'login.html')

    else:
        return render(request, 'org.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'invalid credentials...')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def home(request):
    return render(request, 'home.html')


def viewdoor(request):
    doors = Door.objects.all()

    return render(request, 'viewdoors.html', {'doors': doors})


def adddoor(request):

    if request.method == 'POST':
        floor = request.POST.get('floor')
        name = request.POST.get('name')
        reader = request.POST.get('reader')

        try:
            door = Door(floor=floor, name=name, reader=reader)
            door.save()
            messages.success(request, "Door Added Successfully.")
            return render(request, 'addDoor.html')
        except :
                messages.error(request, "Something Went Wrong!!!")
                return render(request, 'addDoor.html')

    return render(request, 'addDoor.html')


def addreader(request):
    if request.method == 'POST':
        model = request.POST.get('model')
        macid = request.POST.get('macid')
        doorlock = request.POST.get('doorlock')

        try:
                reader = Reader(model=model, macID=macid, doorlocked=doorlock)
                reader.save()
                messages.success(request, "Reader Added Successfully.")
        except:
                messages.error(request, "Something Went Wrong!!!")
                return render(request, 'addreader.html')

    return render(request, 'addReader.html')


@api_view(['GET'])
def registerReader(request):
    macid = request.GET['mac']

    if Reader.objects.filter(macID=macid).exists():
        return Response("Reader Already Exists!!!", status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        mac = Reader(macID=mac)
        mac.save()

    return Response("successfully Register!!!", status=status.HTTP_201_CREATED)


@api_view(['GET'])
def Keeplive(request):
    macid = request.GET['mac']

    if Reader.objects.filter(macID=macid).exists():
        mac = Reader.objects.get(macID=macid)
        mac.lastseen = datetime.now()
        mac.save(update_fields=['lastseen'])

        return Response("last seen updated!!!", status=status.HTTP_201_CREATED)
    else:
        pass
    return Response("Some thing went wrong!!!", status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def attendance(request):
    cardid = request.GET['cardid']
    macid = request.GET['mac']

    checkin = Checkin(cardid=cardid, macID=macid)
    checkin.save()

    return Response("checkin!!!", status=status.HTTP_201_CREATED)


def viewreader(request):
    reader = Reader.objects.all()

    return render(request, 'viewReaders.html', {'reader': reader})

#
def adduser(request):
    dept = Department.objects.all()
    desg = Designation.objects.all()

    if request.method == 'POST':
        name = request.POST.get('uname')
        cardid = request.POST.get('cardid')
        dep_id = request.POST.get('Department')
        desg_id = request.POST.get('Designation')
        try:
            department = Department.objects.get(pk=dep_id)
            designation = Designation.objects.get(pk=desg_id)
            adduser = User(name=name, cardid=cardid, designation=designation, department=department)
            adduser.save()
            messages.success(request, "User Added Successfully")
            return render(request, 'addUser.html')
        except:
                messages.error(request,"something Went Wrong!!!")
                return render(request, 'addUser.html')
    return render(request, 'addUser.html', {'dept': dept, 'desg': desg})


def viewuser(request):
    users = User.objects.all()

    card=Card.objects.filter(status=0)
    print(card)
    context={
        'users': users,

    }
    return render(request, 'viewuser.html', context)


def edit_user(request,users_id):

    user=User.objects.get(id=users_id)

    cards=Card.objects.filter(status=0)

    context={
        'user':user,
        'cards':cards,
    }
    print(user)
    return render(request, 'edit_user.html',context)

def edit_user_save(request):
    if request.method == 'POST':
        users_id=request.POST.get('users_id')
        stud_name=request.POST.get('sname')
        iscardid= request.POST.get('cardid')



        cardid=Card.objects.get(id=iscardid)
        student=User.objects.get(id=users_id)
        student.card_id=cardid
        student.status=1
        student.save()
        cardid.status=1
        cardid.save()

        return redirect('viewuser')
    else:
         return render(request, 'edit_user.html')









def addDepartment(request):
    if request.method == 'POST':
        department = request.POST.get('Department')

        dept = Department(department_name=department)
        dept.save()
        print(department)
        return render(request, 'addDepartment.html')
    else:
        return render(request, 'addDepartment.html')


def viewDepartment(request):
    return render(request, 'viewDepartment.html')


def addDesignation(request, ):
    dept = Department.objects.all()

    if request.method == 'POST':
        designation = request.POST.get('designation')
        dept_id = request.POST.get('Department')

        department = Department.objects.get(pk=dept_id)

        add_designation = Designation(desg_name=designation, department=department)
        add_designation.save()
        return render(request, 'addDesignation.html')
    else:
        return render(request, 'addDesignation.html', {'dept': dept})


def viewDesignation(request):
    desg = Designation.objects.all()

    return render(request, 'viewDesignation.html', {'desg': desg})


def importCard(request):

    return render(request, 'importCard.html')




def addCard(request):
    current_datetime = datetime.now()
    current_year = current_datetime.year
    current_month = current_datetime.month
    today = date.today()

    if request.method == 'POST':

        file = request.FILES['files']
        csv_reader = pd.read_csv(file)

    try:
        for row in csv_reader.iterrows():

            impcard = Card(cardid=row['cardid'],import_date=today,status=0)
            impcard.save()
            messages.success(request,"Import Successfully")
            return render(request, 'importCard.html')
    except:
        messages.error(request, "Card ID Already Exists!!!")
        return render(request, 'importCard.html')

    return render(request, 'importCard.html')


def viewCard(request):

    return render(request, 'viewCard.html')


def import_students(request):
    if request.method == 'POST':

        file = request.FILES['files']
        csv_reader = pd.read_csv(file)

        for index, row in csv_reader.iterrows():
            impcard = User(student_id=row['id'],name=row['name'])
            impcard.save()

        return render(request, 'addUser.html')
    else:
        return render(request, 'addUser.html')