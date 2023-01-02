from django import forms
from students.models import Student, Course


class CourseForm(forms.ModelForm):
   Cname= forms.CharField( max_length=200, required=False)
   class Meta: 
      model = Course
      fields = '__all__' 



class StudentForm(forms.ModelForm):
   roll_no = forms.IntegerField( required=False)
   First_name = forms.CharField(max_length=200, required= False)
   Last_name = forms.CharField(max_length=200, required= False)
   Cname = forms.ModelChoiceField(queryset = Course.objects.all(),required=True)
   class Meta: 
      model = Student
      fields = ['Cname', 'roll_no', 'First_name', 'Last_name']
  
   
      
      