from django.db import models

# Create your models here.

class Student(models.Model):
    # id= models.AutoField()#automatically created by django
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    address= models.TextField()
    email = models.EmailField(null=True, blank=True)
    # dob= models.DateTimeField()
    # file = models.FileField(upload_to=None, max_length = 100)
    def __str__(self)->str:
         return self.name
class Car(models.Model):
    name = models.CharField(max_length = 100)
    speed = models.IntegerField(default=50)
    def __str__(self)->str:
         return self.name

































#     >>> from home.models import *  
# >>> Student
# <class 'home.models.Student'>
# >>> Student.objects.all()
# <QuerySet []>
# >>>
# >>> s1= Student(name="shashank",age=23,address="6/3D Shastri Nagar,Khandari",email="shashank@gmail.com") 🌟CREATE Operation
# >>> s1
# <Student: Student object (None)>
# >>> s1.save()🌟Data Created
# >>> s1🌟Data READ
# <Student: Student object (1)>
# >>> s1.name🌟 READ Operation
# 'shashank'
# >>> s1.age🌟  READ Operation
# 23