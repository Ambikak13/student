

from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from . views import say, some, adm, std, stf, prnt, sl, sfl, pl, add, addrecord, per_info, pinfo, sachiev, sachievment, rgstr, signin,student_apply_leave,student_apply_leave_save
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path("id/", say, name="ref"),
    path("ids/", sl, name="ref"),
    path("idsf/", sfl, name="ref"),
    path("idp/", pl, name="ref"),


    path("", some, name="Admin"),
    
    path("ad/", adm, name="admin"),
    path("st/", std, name="staff"),
    path("sf/", stf, name="student"),
    path("pt/", prnt, name="parent"),

#   path("ins/", inst, name="ref"),
# addstudent

    path('add/', add, name='add'),
    path('add/addrecord/', addrecord, name='addrecord'),

# personalinfo page

    path('per_info/', per_info, name='per_info'),
    path('per_info/pinfo/', pinfo, name='pinfo'),

# achievment page

    path('sachiev/', sachiev, name='sachiev'),
    path('sachiev/sachievment/', sachievment, name='sachievment'),

# Registerpage
    path('rg/', rgstr, name='ref'), 

# signin

    path('signin/', signin, name='signin'),
#student
    path('student_apply_leave/',student_apply_leave,name='studentleave'),
     path('student_apply_leave_save/',student_apply_leave_save,name='studentleavesave')

    

]

