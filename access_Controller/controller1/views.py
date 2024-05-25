from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'index.html')

def organization(request):

    return render(request,'org.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render (request,'home.html')

def viewdoor(request):
    return render (request,'viewdoors.html')

def adddoor(request):
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