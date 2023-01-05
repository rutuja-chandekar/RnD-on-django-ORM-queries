from django.db import models

class Course(models.Model):
    Cname= models.CharField(max_length=200, blank=True, null=True)
    Ccode= models.IntegerField(default= 0)
    def __str__(self): 
        return self.Cname

class Student(models.Model):
    
    Cname = models.ForeignKey(Course, blank=True,null=True, on_delete=models.CASCADE)
    roll_no = models.IntegerField(default= 0)
    First_name = models.CharField(max_length=200, blank=True, null=True)
    Last_name = models.CharField(max_length=200, blank=True, null=True)
    marks = models.IntegerField(default= 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f' { self.First_name } {self.Cname} '
    

  
    

    
