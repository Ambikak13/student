
from django.http import HttpResponse
from django.template import loader
from tkinter import messagebox
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .models import stud
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from Myapp.EmailBackEnd import EmailBackEnd
from .models import leave
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


def add(request):
  template = loader.get_template('s1/addstudent.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  rn = request.POST['rno']
  fn = request.POST['first']
  ln = request.POST['last']
  cl=request.POST['clss']
  sc=request.POST['sec']
  stud1 = stud(rno=rn, firstname=fn, lastname=ln, sclass=cl, section=sc)
  stud1.save()
  

# return HttpResponse("inserted successfully")
  return HttpResponseRedirect(reverse('add'))   


# personal info
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

# registration form
def rgstr(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['password']
        if get_user_model().objects.filter(username = uname).exists():
                messages.success(request,"Already exist")
        else:
            user=get_user_model().objects.create_user(username=uname,first_name=fname,last_name=lname,password=password)
            user.save()
            if user is not None:
                auth.login(request,user)
                messages.success(request,'Successfully Registered now you can login!')
            else:
             return HttpResponse("password does not matched")
    
    return render(request,'s1/register.html')

# login_page     

def signin(request):

  if request.method == 'POST':
    user=get_user_model().objects.get(user=request.POST['uname'])
    print(user)

  #   if user is not None:
  #     login(request, user)
  #     user_type_data=user.user_type_data
  #     if user_type_data== '1':
  #       return redirect('admin')
  #     elif user_type_data== '2':
  #       return redirect('staff')
  #     elif user_type_data== '3':
  #       return redirect('student')
  #     elif user_type_data== '4':
  #       return redirect('parent')
      
  #     messages.success(request,'logged in successfully')
  #     print("matched")
  #   else:
  #     messages.error(request, "incorrected password username")
  #     print("not matched")
  #     return redirect("Admin")
    return render(request,'s1/admin.html')
  return HttpResponse(request,"not match")

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

  