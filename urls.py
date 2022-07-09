

from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from . views import add_aadvisor, add_aadvisor_save, add_staff, say, some, adm, std, stf, prnt, sl, sfl, pl, add, addrecord, per_info, pinfo, sachiev, sachievment, rgstr, signin,add_course,add_course_save,add_class,add_class_save,add_subject,add_subject_save,add_staff_save,add_staff,time_table,take_attendance,attendance_save,add_aadvisor,add_aadvisor_save
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
# hod
    path('add_staff',add_staff,name='addcourse'),
    path('add_staff_save',add_staff_save,name='addcoursesave'),
    path('add_course',add_course,name='addcourse'),
    path('add_course_save',add_course_save,name='addcoursesave'),
    path('add_class',add_class,name='addcourse'),
    path('add_class_save',add_class_save,name='addcoursesave'),
    path('add_subject',add_subject,name="addsubject"),
    path('add_subject_save',add_subject_save,name='addacademicadvisor'),
    path('add_aadvisor',add_aadvisor,name="addsubject"),
    path('add_aadvisor_save',add_aadvisor_save,name='addacademicadvisorsave'),
    path('add/', add, name='add'),
    path('add/addrecord/', addrecord, name='addrecord'),
    path('time_table',time_table,name='addcourse'),
# personalinfo page

    path('per_info/', per_info, name='per_info'),
    path('per_info/pinfo/', pinfo, name='pinfo'),

# staff
    path('take_attendance',take_attendance,name="take_attendance"),
    path('attendance_save',attendance_save,name="fetch_student"),
    path('sachiev/', sachiev, name='sachiev'),
    path('sachiev/sachievment/', sachievment, name='sachievment'),

# Registerpage
    path('rg/', rgstr, name='ref'), 

# signin

    path('signin/', signin, name='signin'),
#student
    

    

]

