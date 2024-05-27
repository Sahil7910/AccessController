from django.shortcuts import render
from controller1.models import Door
from django.contrib import messages

# Create your views here.
def index(request):



    return render (request,'index.html')

def organization(request):

    if request.method== 'POST':
        orgname=request.POST['orgname']
        orgid=request.POST['orgid']



        print("orgname:",orgname, "OrgID:",orgid)
        return render (request,'login.html')

    else:
            return render (request, 'org.html')

def login(request):
    return render(request,'login.html')

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

    
    return render(request,'addReader.html')

def viewreader(request):
    return render (request,'viewReaders.html')



def adduser(request):
    return render (request,'addUser.html')

def viewuser(request):
    return render(request,'viewuser.html')

def addDepartment(request):
    return render(request,'addDepartment.html')

def viewDepartment(request):
    return render (request,'viewDepartment.html')

def addDesignation(request):
    return render(request,'addDesignation.html')

def viewDesignation(request):
    return render (request,'viewDesignation.html')


def addCard(request):
    return render(request,'addCard.html')

def viewCard(request):
    return render (request,'viewCard.html')