import imp
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
# Create your models here.

sex_choice = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class CustomUser(models.Model):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    REQUIRED_FIELDS = ('user',)
    USERNAME_FIELD= 'user'

# Create your models here.
class stud(models.Model):
    rno = models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sclass = models.CharField(max_length=25)
    section  = models.CharField(max_length=10)
    gender = models.CharField(max_length=50, choices=sex_choice, default='Male')
    DOB = models.DateField(default='1998-01-01')
    academic_advisor=models.CharField(max_length=25)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    address= models.CharField(max_length=50)
    achievements=models.CharField(max_length=100)
    scholarship=models.CharField(max_length=50)
    fees=models.CharField(max_length=10)
    midday_meal=models.CharField(max_length=20)
    objects = models.Manager()

class hod(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects = models.Manager()

class parent(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    objects = models.Manager()

class classes(models.Model):
    class_id=models.AutoField(primary_key=True)
    sclass=models.CharField(max_length=15)
    objects = models.Manager()

class courses(models.Model):
    course_id=models.CharField(primary_key=True,max_length=20)
    course=models.CharField(max_length=25)
    fees=models.CharField(max_length=10)
    objects = models.Manager()

class subjects(models.Model):
    subject_id=models.CharField(primary_key=True,max_length=20)
    class_id=models.ForeignKey(classes,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    course_id=models.ForeignKey(courses,on_delete=models.CASCADE)
    objects = models.Manager()

class mark(models.Model):
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subjects,on_delete=models.CASCADE)
    marks=models.CharField(max_length=3)
    category=models.CharField(max_length=20)
    objects = models.Manager()

class attendance(models.Model):
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    month=models.CharField(max_length=15)
    subject_id=models.ForeignKey(subjects,on_delete=models.CASCADE)
    class_held=models.CharField(max_length=3)
    class_attended=models.CharField(max_length=3)
    objects = models.Manager()

class application(models.Model):
    rno=models.AutoField(primary_key=True)
    distance=models.CharField(max_length=3)
    income_status=models.CharField(max_length=10)
    objects = models.Manager()

class eccc(models.Model):
    eccc_course=models.CharField(max_length=25)
    no_of_seats=models.CharField(max_length=10)
    objects = models.Manager()

class notification(models.Model):
    notification_id=models.CharField(primary_key=True,max_length=20)
    info=models.CharField(max_length=50)
    sender=models.CharField(max_length=25)
    recieve=models.CharField(max_length=25)
    contact=models.CharField(max_length=10)
    objects = models.Manager()

class leave(models.Model):
    leave_id=models.CharField(primary_key=True,max_length=20)
    rno=models.ForeignKey(stud,on_delete=models.CASCADE)
    purpose=models.CharField(max_length=100)
    leave_date=models.DateField()
    objects = models.Manager()
   
class staff(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    staff_id=models.CharField(primary_key=True,max_length=20)
    staff_name=models.CharField(max_length=25)
    dept=models.CharField(max_length=25)
    objects = models.Manager()

class subject_handled(models.Model):
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subjects,on_delete=models.CASCADE)
    objects = models.Manager()

@receiver(post_save,sender=CustomUser)
def createprofile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type_data==1:
            hod.objects.create(admin=instance)
        if instance.user_type_data==2:
            staff.objects.create(admin=instance)
        if instance.user_type_data==3:
            stud.objects.create(admin=instance)
        if instance.user_type_data==4:
            parent.objects.create(admin=instance)

@receiver(post_save,sender=CustomUser)
def saveprofile(sender,instance,created,**kwargs):
    if instance.user_type_data==1:
        instance.hod.save()
    if instance.user_type_data==2:
         instance.staff.save()   
    if instance.user_type_data==3:
         instance.stud.save()   
    if instance.user_type_data==4:
         instance.parent.save()   