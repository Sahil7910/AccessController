from django.urls import path
from controller1 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("org",views.organization, name="organization"),
    path("login",views.login, name="login"),
    path("home",views.home, name="home"),
    path("viewdoors",views.viewdoor,name="viewdoor"),
    path("adddoor",views.adddoor,name="adddoor"),
    path("addreader",views.addreader,name="addreader"),
    path("viewreader",views.viewreader,name="viewreader"),
    path("adduser", views.adduser,name="adduser"),
    path("viewuser", views.viewuser,name="viewuser"),
    path("addDepartment", views.addDepartment,name="addDepartment"),
    path("viewDepartment", views.viewDepartment,name="viewDepartment"),
    path("addDesignation", views.addDesignation,name="addDesignation"),
    path("viewDesignation", views.viewDesignation,name="viewDesignation"),
    path("addCard", views.addCard,name="addCard"),
    path("viewCard", views.viewCard,name="viewCard"),
]
