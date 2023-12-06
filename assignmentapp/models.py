from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(User,blank=True,default=True,on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    contact = models.CharField(max_length = 10)
    faculty = models.CharField(max_length = 10,choices=(('BIT','BIT'),
                                                        ('B.Sc CSIT','B.Sc CSIT')))
    rollno = models.CharField(max_length = 15)
    semester = models.CharField(max_length = 10,choices = (('1st','1st'),
                                                            ('2nd','2nd'),
                                                            ('3rd','3rd'),
                                                            ('4th','4th'),
                                                            ('5th','5th'),
                                                            ('6th','6th'),
                                                            ('7th','7th'),
                                                            ('8th','8th')))
    section = models.CharField(max_length = 10,choices=(('A','A'),
                                                        ('B','B')))
    
    def __str__(self):
        return self.name 

class Teacher(models.Model):
    user = models.ForeignKey(User,blank=True,default=True,on_delete=models.CASCADE)
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    contact = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.name 

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    uploadedDate = models.DateField(auto_now_add=True,null=True,blank=True)  
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignments/')
    status = models.CharField(max_length = 10,choices = (('Checked','Checked'),
                                                        ('Submitted','Submitted')),default='Submitted')
    remarks = models.TextField(default="No Remarks")

    def __str__(self):
        return self.title


