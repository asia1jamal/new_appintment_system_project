from django.shortcuts import render
from contextlib import _RedirectStream
from pstats import Stats
import statistics
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.http import *
from django.contrib import auth
from rest_framework.response import Response 
from rest_framework import decorators
from django.http import HttpResponse
from rest_framework.decorators import  api_view
from doctor.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.contrib.auth import *
from django.db.models import Q
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

#PATIENTS VIEWS

@api_view(['POST'])
def create_new_paient(request):
    idNum=request.data['idNum']
    #user_name=request.data['username']
    firstName=request.data['firstName']
    middleName=request.data['middleName']
    lastName=request.data['lastName']
    gender=request.data['gender']
    email=request.data['email']
    birthdate=request.data['birthdate']
    password=request.data['password']
    phoneNum=request.data['phoneNum']
    patient=User.objects.create_user(idNum=idNum,email=email,password=password)

    if patient is not None:
        patient.save()
   
    p=Patient.objects.create(
    
                             idNum=idNum,
                             firstName=firstName,
                             middleName=middleName,
                             lastName=lastName,
                             gender=gender,
                             birthdate=birthdate,
                             phoneNum=phoneNum,
                             email= email,
                             password= password
                             )
    if Patients:
        Patients.save()
    Token.objects.create(patient=patient)

   # ser=Patientserilizers(p,many=False)
    return Response(request.data)


@api_view(['POST'])
def create_new_Doctor(request):
    idNum=request.data['idNum']
    #user_name=request.data['username']
    firstName=request.data['firstName']
    middleName=request.data['middleName']
    lastName=request.data['lastName']
    gender=request.data['gender']
    email=request.data['email']
    birthdate=request.data['birthdate']
    password=request.data['password']
    phoneNum=request.data['phoneNum']
    doc=User.objects.create_user(idNum=idNum,email=email,password=password)

    if doc is not None:
        doc.save()
   
    d=Doctors.objects.create(
    
                             idNum=idNum,
                             firstName=firstName,
                             middleName=middleName,
                             lastName=lastName,
                             gender=gender,
                             birthdate=birthdate,
                             phoneNum=phoneNum,
                             email= email,
                             password= password
                             )
    if Doctors:
        Doctors.save()
    Token.objects.create(doc=doc)

   # ser=Patientserilizers(p,many=False)
    return Response(request.data)

       
@api_view(['GET'])
def getVacc(request):
    vacc=Vaccine.objects.all()
    ser = Vaccineserilizer(vacc,many=True)
    return Response(ser.data)

@api_view(['GET'])
def getVaccByID(request,pk):
    vacc=Vaccine.objects.get(id=pk)
    ser=Vaccineserilizer(vacc,many=False)
    return Response(ser.data)


@api_view(['GET'])
def doctors_list(request):
    doctor_list=Doctor.objects.all()
    Doc_ser=doctorsserilizer(doctor_list,many=True)
    return Response(Doc_ser.data)

@api_view(['GET'])
#@authentication_classes([TokenAuthentication,BaseAuthentication,SessionAuthentication])
#@permission_classes([IsAuthenticated])
def Show_my_Appointments(request):
    Current_Patient=request.user.id
    my_Appointments=BookedAppoiments.objects.filter(by_user=Current_Patient)
    p_ser=bookedAppoimentserilizers(my_Appointments)
    if p_ser :
        return Response(p_ser.data)
    else:
        return Response(" YOU HAVE NO APPOINTMENTS YET")


@api_view(["POST"])
#@authentication_classes([TokenAuthentication,BaseAuthentication,SessionAuthentication])
#@permission_classes([IsAuthenticated])
def BookAppointment(request,id):
    current_Appointment=BookedAppoiments.objects.get(pk=id)
    current_Patient=request.user.id
    current_Date=current_Appointment.Date
    if current_Date is not None:
        ser= bookedAppoimentserilizers(current_Appointment)
        return Response(ser.data)
    else:
         return Response("APPOINTMENT NOT AVAILABLE")
    if online_chices is not None:
            current_Patient=request.user.id
            current_Date=current_Appointment.date


@api_view(['POST'])
#@authentication_classes([TokenAuthentication,BasicAuthentication,SessionAuthentication])
def createNewAppoinment(request):
    current_Doctor=request.user.id
    select_Location_Id=request.data['Location']
    date=request.date['date']
    begin_time=request.data['begin_time']
    finish_time=request.data['finish_time']

    new_Appointment=DoctorsAppointment(
        by_Doctor_id=current_Doctor,
        LocationOfAppoiment=select_Location_Id,
        date=date,
        begin_time=begin_time,
        finish_time=finish_time
    )
    new_Appointment.save()
    App=DoctorsAppointmentserilizer(new_Appointment)
    return Response(App.data)






"""{
       "idNum":"123",
       " firstName":"asia",
        "middleName":"fdfds",
         "lastName":"fff",
          "gender":"female",
          "birthdate":"2010",
          "phoneNum":"8888",
          "email":"a@gmail.com",
          "password":"111",
}"""

@api_view(['GET'])
def geAlltPatient(request):
    p=Patient.objects.all()
    ser=Patientserilizers(p,many=True)
    return Response(ser.data)

