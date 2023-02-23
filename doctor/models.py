from django.db import models
from django.dispatch import receiver #جهة مستقبلة للتعليمات
from rest_framework.authtoken.models import Token 
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import django.utils.timezone


class Patient(models.Model):
    idNum=models.OneToOneField(User,on_delete=models.CASCADE)
    firstName=models.CharField(max_length=10)
    middleName=models.CharField(max_length=25,blank=False,null=False)
    lastName=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField(blank=True,null=True)
    birthdate=models.DateField(blank=True,null=True)
    password=models.CharField(max_length=10)
    phoneNum=models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
class Doctor(models.Model):
    idNum=models.OneToOneField(User,on_delete=models.CASCADE)
    firstName=models.CharField(max_length=10)
    middleName=models.CharField(max_length=25,blank=False,null=False)
    lastName=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField(blank=True,null=True)
    birthdate=models.DateField(blank=True,null=True)
    password=models.CharField(max_length=10)
    phoneNum=models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    

class DoctorInfo(models.Model):
    EducationsLiences=models.TextField(max_length=100)
    DocImage=models.ImageField(upload_to='images')

class PatientInfo(models.Model):
    EducationsLiences=models.TextField(max_length=100)
    DocImage=models.ImageField(upload_to='images')

class DoctorsAppointment(models.Model):
    DoctorName=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    DateOfAppoiment=models.DateField(blank=True,null=True)
    LocationOfAppoiment=models.CharField(max_length=30)
    date=models.DateField(blank=True,null=True)
    begin_time=models.DateTimeField(blank=True,null=True)
    finish_date=models.DateTimeField(blank=True,null=True)
    Online=models.BooleanField()


class BookedAppoiments(models.Model):
    doctorName=models.ForeignKey(Doctor,related_name='appointment',on_delete=models.CASCADE)
    PatientName=models.ForeignKey(Patient,related_name='appointment',on_delete=models.CASCADE)
    LOCATION_CHOICES=(
        ('Khartoum','Khartoum'),
        ('Bahri','Bahri'),
        ('Omdorman','Omdorman')
    )
    location=models.CharField(max_length=12,choices=LOCATION_CHOICES)
    Date=models.DateField(blank=True,null=True)
    time=models.DateTimeField(blank=True,null=True)



class Vaccine(models.Model):
    VaccID=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=255)
    Age=models.IntegerField()
    WhatBefor=models.CharField(max_length=255)
    WhatAfter=models.CharField(max_length=255)
    WhatToDo=models.CharField(max_length=255)
    Symptoms=models.CharField(max_length=255)
    LOCATION_CHOICES=(
        ('Khartoum','Khartoum'),
        ('Bahri','Bahri'),
        ('Omdorman','Omdorman')
    )
    location=models.CharField(max_length=12,choices=LOCATION_CHOICES)

class VaccineLocations(models.Model):
    Bahri=models.CharField(max_length=100000)
    Khartoum=models.CharField(max_length=100000)
    OmDurman=models.CharField(max_length=100000)
