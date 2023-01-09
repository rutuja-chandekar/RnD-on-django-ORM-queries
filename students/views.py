from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from students.models import *
from students.forms import CourseForm, StudentForm, forms 
from django.shortcuts import redirect
from django.urls import reverse
import logging, traceback


logger = logging.getLogger('  django')

class index(View):
    def get(self, request):
        val={'response': 'user added'}
        print('hello')
        logger.info ('SOme message')
        return HttpResponse(val, status=200)

class studentView (View):
    def get(self, request):
        studentlist = Student.objects.all()
        courselist = Course.objects.all()
        print(studentlist, courselist)
        return render(request, "students/studentlist.html", context= {'studentlist': studentlist, 'courselist': courselist})
    
class Add_student(View):
    def get(self, request):
        courselist= Course.objects.all()
        print(courselist)
        return render(request, "students/Add_student.html", context= {'courselist': courselist})
        
    def post(self, request):
       
            Mystudent = StudentForm(request.POST) 
            if Mystudent.is_valid():
             
                Mystudent.save()
               
                     
             
                return redirect(reverse('students:studentView'))
            else:
                print(Mystudent.errors)
            
            return render(request, "students/Add_student.html", context= { })
        
    
class delete_student(View):
    def get(self, request, id):
        obj = Student.objects.get(pk=id)
        obj.delete()
        return redirect(reverse('students:studentView'))
 
 
    
class update(View):
    def get(self, request,id):
        Student_obj = Student.objects.get(pk=id)
        courselist= Course.objects.all()
        return render(request, "students/update.html", context= {'Student_obj' : Student_obj, 'courselist': courselist})
    
    def post(self, request,id):
        obj = Student.objects.get(pk=id)
        
        Mystudent = StudentForm(request.POST, instance=obj)
        
         
        
        if Mystudent.is_valid():
            Mystudent.save()
          
            print('Your account has been updated!')
        return redirect(reverse('students:studentView'))
          
class courselist(View):
    def get(self, request):
        courselist = Course.objects.all()
        print(courselist)
        return render(request, "students/courselist.html", context= {'courselist': courselist})   
    def post(self,request):
        pass 

class Add_Course(View):
    def get(self, request):
        return render(request, "students/Add_course.html", context= {})
    
    def post(self, request):
            
            MyCourse =CourseForm(request.POST)
             
            if MyCourse.is_valid():
                

                MyCourse.save()
                return redirect(reverse('students:courselist'))
            else:
                print(MyCourse.errors)
            
            return render(request, "students/Add_course.html", context= { })
       
        

class delete_course(View):
    def get(self, request, id):
        obj = Course.objects.get(pk=id)
        obj.delete()
        return redirect(reverse('students:courselist'))
    def post(self, request):
        pass
    
class update_course(View):
    def get(self, request,id):
        course_obj = Course.objects.get(pk=id)
        return render(request, "students/course_update.html", context= {'course_obj' : course_obj})
                
    def post(self, request,id):
        obj = Course.objects.get(pk=id)
        course_obj = Course.objects.get(pk=id)
        Mycourse =CourseForm(request.POST, instance=course_obj)
       
         
        
        if Mycourse.is_valid():
            Mycourse.save()
        
            print('Your account has been updated!')
        return redirect(reverse('students:courselist'))
