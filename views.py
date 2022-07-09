
from email import message
from multiprocessing import context
from tokenize import Name
from urllib import request
from venv import create
from django.http import HttpResponse
from django.template import loader
from tkinter import messagebox
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .models import CustomUser, attendance, classes, stud, subjects
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from Myapp.EmailBackEnd import EmailBackEnd
from .models import leave,courses,staff
# Create your views here.


# login pages html

def say(request):
    return render(request,'s1/s2.html')

def sl(request):
    return render(request,'s1/studentlogin.html')

def sfl(request):
    return render(request,'s1/stafflogin.html')

def pl(request):
    return render(request,'s1/parentlogin.html')

# home page 

def some(request):
    return render(request,'s1/index.html')

# admin staff student page html

def adm(request):
    return render(request,'s1/admin.html')
  
def stf(request):
    return render(request,'s1/staff.html')

def std(request):
    return render(request,'s1/student.html')

def prnt(request):
    return render(request,'s1/parent.html')

# insert page

def pl(request):
  return render(request,'s1/parentlogin.html')

#def inst(request):
    #return render(request,'s1/addstudent.html')

# registration form
def rgstr(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['password']
        email=request.POST['email']
        usertype=request.POST['usertype']
        if get_user_model().objects.filter(username = uname).exists():
                messages.success(request,"Already exist")
        else:
            user=get_user_model().objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password,user_type=usertype)
            user.save()
            if user is not None:
                auth.login(request,user)
                messages.success(request,'Successfully Registered now you can login!')
            else:
             return HttpResponse("password does not matched")
    
    return render(request,'s1/register.html')

# login_page     

def signin(request):
  if request.method=="POST":
    user=EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'),)
    print("authenticated")      
    if user is not None:
        login(request,user)
        print(user)
        user_type=user.user_type
        if user_type =='1':
          return render(request,"s1/admin.html")          
        elif user_type =='2':
          return render(request,"s1/staff.html") 
        elif user_type =='3':
          return render(request,"s1/student.html")
        elif user_type =='4':
          return render(request,"s1/parent.html") 
        else:
          messages.error(request,"Emil and password are invalid")
          return redirect("signin")
    else:
        messages.error(request,"Emil and password are invalid")            
        return redirect("signin")
  return HttpResponse()

#add student
def add(request):
  course=courses.objects.all()
  cls=classes.objects.all()
  context={
    'course':course,
    'cls':cls
  }
  return render(request,'s1/addstudent.html',context)


def addrecord(request):
  rn = request.POST['rno']
  fn = request.POST['first']
  ln = request.POST['last']
  gn=request.POST['gender']
  cl=request.POST['cls']
  sc=request.POST['sec']
  s_start=request.POST['sessions']
  s_end=request.POST['sessione']
  cs=request.POST['course']
  stud1 = stud(rno=rn, first_name=fn, last_name=ln,gender=gn,sclass=cl,section=sc,session_start=s_start,session_end=s_end,course=cs)
  stud1.save()
  stud1=stud
  

# return HttpResponse("inserted successfully")
  return HttpResponseRedirect(reverse('add'))   

#add course
def add_course(request):
  return render(request,"s1/addcourse.html")

def add_course_save(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
   
  else:
    course=request.POST.get("Name")
    cid=request.POST.get("course_id")
    fee=request.POST.get("fees")
    try:
      course_model=courses(course_id=cid,Name=course,fees=fee)
      course_model.save()
      print("Successfuly added course")
      return HttpResponse(request,"Successfuly added course")
      return HttpResponseRedirect("s1/add_course")
    except:
      print("faild to added course")
      return HttpResponse(request,"Failed to add course")
      return HttpResponseRedirect("s1/add_course")

def add_class(request):
  return render(request,"s1/addclass.html")

def add_class_save(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
   
  else:
    cls=request.POST.get("name")
    cid=request.POST.get("class_id")
    try:
      classs_model=classes(class_id=cid,name=cls)
      classs_model.save()
      print("Successfuly added class")
      return HttpResponse(request,"Successfuly added course")
      return HttpResponseRedirect("s1/add_course")
    except:
      print("faild to added course")
      return HttpResponse(request,"Failed to add course")
      return HttpResponseRedirect("s1/add_course")

#add subject

def add_subject(request):
  staffs=staff.objects.all()
  cls=classes.objects.all()
  context={
    'staffs':staffs,
    'cls':cls
  }
  return render(request,'s1/addsubject.html',context)

def add_subject_save(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
   
  else:
    sname=request.POST.get("subject")
    subid=request.POST.get("subject_id")
    id=request.POST.get("staffs")
    staffs=staff.objects.get(staff_id=id)
    clid=request.POST.get("cls")
    cls=classes.objects.get(class_id=clid)
    try:
      subject=subjects(subject_id=subid,subject=sname,class_id=cls,staff_id=staffs)
      subject.save()
      print("Successfuly added subject")
      return HttpResponse(request,"Successfuly added subject")
      return HttpResponseRedirect("s1/add_course")
    except:
      print("faild to added course")
      return HttpResponse(request,"Failed to add course")
      return HttpResponseRedirect("s1/add_course")

def add_staff(request):
  course=courses.objects.all()
  return render(request,"s1/addstaff.html",{"course":course})

def add_staff_save(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
   
  else:
    sid=request.POST.get("staff_id")
    sname=request.POST.get("staff_name")
    id=request.POST.get("course")
    course=courses.objects.get(course_id=id)
    
    try:
      staff_model=staff(staff_id=sid,staff_name=sname,course_id=course)
      staff_model.save()
      print("Successfuly added class")
      return HttpResponse(request,"Successfuly added staff")
      return HttpResponseRedirect("s1/add_course")
    except:
      print("faild to added course")
      return HttpResponse(request,"Failed to add staff")
      return HttpResponseRedirect("s1/add_course")

def add_aadvisor(request):
    staffs=staff.objects.all()
    cls=classes.objects.all()
    context={
    'staffs':staffs,
    'cls':cls,
    #'studn':studn
  }
    return render(request,"s1/addacademicadvisor.html",context)
def add_aadvisor_save(request):
    clss=request.POST.get("cls")
    studn=stud.objects.filter(sclass=clss)

    return render(request,"s1/assignacademicadvisor.html",{"studn":studn}) 

def take_attendance(request):
  subject=subjects.objects.all()
  cls=classes.objects.all()
  student=stud.objects.all()
  context={
    'subject':subject,
    'cls':cls,
    'student':student
  }
  return render(request,"s1/takeattendance.html",context)

def attendance_save(request):
  if request.method!="POST":
    return HttpResponse(request,"Method not allowd")
   
  else:
    sid=request.POST.get("student")
    student=stud.objects.get(rno=sid)
    id=request.POST.get("subject")
    subject=subjects.objects.get(subject_id=id)
    ch=request.POST.get("cheld")
    ca=request.POST.get("cattend")
    frm=request.POST.get("from")
    to=request.POST.get("to")
    try:
      attend=attendance(rno=student,subject_id=subject,class_held=ch,class_attend=ca,From=frm,To=to)
      attend.save()
      print("Successfuly added attendance")
      return HttpResponse(request,"Successfuly added staff")
      return HttpResponseRedirect("s1/add_course")
    except:
      print("faild to added course")
      return HttpResponse(request,"Failed to add staff")
      return HttpResponseRedirect("s1/add_course")
def time_table(request):
  return render(request,"s1/timetable.html")

#personal info
def per_info(request):
  template = loader.get_template('s1/personalinfo.html')
  return HttpResponse(template.render({}, request))

def pinfo(request):
  rno = request.POST['rno']
  fn = request.POST['first']
  ln = request.POST['last']
  fname=request.POST['fname']
  mname=request.POST['mname']
  cno=request.POST['cno']
  eml=request.POST['eml']
  addr=request.POST['addr']
  gn=request.POST['gn']
  dob=request.POST['dob']
  stud1=stud.objects.get(rno=rno)
  stud1.rno=rno
  stud1.firstname=fn
  stud1.lastname=ln
  stud1.fname=fname
  stud1.mname=mname
  stud1.contact=cno
  stud1.email=eml
  stud1.address=addr
  stud1.sex=gn
  stud1.DOB=dob
  #stud1 = stud(rno=rno, firstname=fn, lastname=ln, fname=fname, mname=mname, contact=cno, email=eml, address=addr )
  stud1.save()
  messages.success(request, 'Record inserted successfully!')
# return HttpResponse("inserted successfully")
  return HttpResponseRedirect(reverse('per_info'))  

# achievments page
def sachiev(request):
  template = loader.get_template('s1/achievment.html')
  return HttpResponse(template.render({}, request))


def sachievment(request):
  rno = request.POST['rno']
  ach = request.POST['achiev']
  stud1=stud.objects.get(rno=rno)
  stud1.achievment=ach
  #stud1 = stud(rno=rno, firstname=fn, lastname=ln, fname=fname, mname=mname, contact=cno, email=eml, address=addr )
  stud1.save()
  messages.success(request, 'Record inserted successfully!')
# return HttpResponse("inserted successfully")
  return HttpResponseRedirect(reverse('sachiev'))  

def student_apply_leave(request):
    student_obj = stud.objects.get(admin=request.user.id)
    leave_data = leave.objects.filter(rno=student_obj)
    context = {
        "leave_data": leave_data
    }
    return render(request, 's1/student_apply_leave.html', context)
    
def student_apply_leave_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('student_apply_leave')
    else:
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student_obj = stud.objects.get(admin=request.user.id)
        try:
            leave_report = leave(student_id=student_obj, leave_date=leave_date, leave_message=leave_message, leave_status=0)
            leave_report.save()
            messages.success(request, "Applied for Leave.")
            return redirect('student_apply_leave')
        except:
            messages.error(request, "Failed to Apply Leave")
            return redirect('student_apply_leave')


def guserdetail(request):
  if request.user!=None:
    return HttpResponse("user:" +request.user.email+ "usertype:" +request.user.user_type_data)
  else:
    return HttpResponse("Please Login first")

  