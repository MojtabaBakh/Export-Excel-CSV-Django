
from django.contrib import admin
from django.urls import path , include
from .views import student_list , student_details , Export_students

name='myapp'

urlpatterns = [
    path('studentlist/', student_list),
    path('studentdetails/<pk>', student_details , name="studentdetails"),
    path('Exportstudent/', Export_students , name="exportstudent"),
    
]