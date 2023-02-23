from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from doctor import views
from rest_framework.authtoken.views import obtain_auth_token
#obtain_auth_token فيو بيعمل aceess للمودل حق الtokens 
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('doctor.urls')),
    path('patientSingup/',views.create_new_paient),
    path('getAllPatient/',views. geAlltPatient),
    path('docSignUp/',views.create_new_Doctor),
    path('vacc/',views.getVacc),
    path('vacc/<str:pk>/',views.getVaccByID),
    path('doctorList/',views.doctors_list),
    path('myAppointments/',views.Show_my_Appointments),
    path('bookAppointment/',views.BookAppointment),
    path('insertnewAppointment/',views.createNewAppoinment),
]
"""
{
        "id": 1,
        "firstName": "asia",
        "middleName": "jamal",
        "lastName": "aldeen",
        "email": "asiajamma@gmail.com",
        "birthdate": "2022-01-12",
        "password": "jamal123",
        "phoneNum": 12345,
        "gender": "F",
        "idNum": 2
    }"""