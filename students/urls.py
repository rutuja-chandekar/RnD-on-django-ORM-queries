from django.contrib import admin
from django.urls import path, include
from students.views import *

app_name= "students"

urlpatterns = [
    path('',studentView.as_view(),name="studentView"),
    path('Add-student/',Add_student.as_view(),name="Add_student"),
    path('update/',update.as_view(),name="update"),  
    path('delete/<int:id>', delete_student.as_view(), name = "delete_student" ),
    path('update/<int:id>', update.as_view(), name = "update" ),
    
    path('courselist/', courselist.as_view(), name="courselist"),
    path('Add-course/',Add_Course.as_view(),name="Add_course"),
    path('update-course/',update_course.as_view(),name="update_course"),  
    path('delete_course/<int:id>', delete_course.as_view(), name = "delete_course" ),
    path('update_course/<int:id>', update_course.as_view(), name = "update_course" ),

   ]

