from django.urls import path
from controller1 import views

urlpatterns = [

    #    path('',views.getData),
    path('register/',views.registerReader),
    path('keep_live/',views.Keeplive),
    path('checkin/',views.attendance),

    path("", views.index, name="index"),
    path("org",views.organization, name="organization"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name='logout' ),
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
    path("importCard", views.importCard,name="importCard"),
    path("addCard", views.addCard,name="addCard"),
    path("viewCard", views.viewCard,name="viewCard"),
    path('edit_user/<users_id>/', views.edit_user, name="edit_user"),
    path('edit_user_save/', views.edit_user_save, name="edit_user_save"),
    path("import_students", views.import_students,name="import_students"),
]
