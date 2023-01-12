from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from students.models import *
from students.forms import CourseForm, StudentForm, forms 
from django.shortcuts import redirect
from django.urls import reverse
import logging, traceback
import os
from django.conf import settings


logger = logging.getLogger(__name__)

class index(View):
    def get(self, request):
        try:
            print(10/0)
            val={'response': 'user added'}
            print('hello')
            logger.info ('SOme message')
            return HttpResponse(val, status=200)
        except:
            logger.error('invalid')

class WebAppListLogsView(View):
    template_name = "students/logs.html"
    print("in the class")

    def get(self, request):
        context = super().get_context_data()
        filepath = open("C:\\Users\\Admin\\Desktop\\django_project\\test_project\\logs\\debug.log")
        log_file_data = filepath.readlines()
        log_data = []; log_details = []
        if log_file_data:
            length = 0
            total_length = len(log_file_data)
            for log in log_file_data:
                length += 1
                if log.startswith('{'):
                    if len(log_details) > 0:
                        log_data.append(log_details)
                    log_details = []
                    log_details.append(log)
                else:
                    log_details.append(log)
                if total_length == length:
                    log_data.append(log_details)
        context['data'] = log_data[::-1]
        context['total_logs'] = len(log_data)
        return render(request, "students/logs.html", context= {'context' : context})
         
        

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print("here  in the def")
    #     filepath = os.path.join(settings.BASE_DIR, "debug3")
    #     print(filepath)
    #     log_file_data = [line.rstrip('\n') for line in open(filepath)]

    #     log_data = []; log_details = []
    #     if log_file_data:
    #         length = 0
    #         total_length = len(log_file_data)
    #         for log in log_file_data:
    #             length += 1
    #             if log.startswith('{'):
    #                 if len(log_details) > 0:
    #                     log_data.append(log_details)
    #                 log_details = []
    #                 log_details.append(log)
    #             else:
    #                 log_details.append(log)
    #             if total_length == length:
    #                 log_data.append(log_details)
    #     context['data'] = log_data[::-1]
    #     context['total_logs'] = len(log_data)
    #     return context

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
