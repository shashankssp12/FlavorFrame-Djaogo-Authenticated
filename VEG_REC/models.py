from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Recipe(models.Model):
    # id=models.AutoField()
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Rname=models.CharField(max_length=120)
    description=models.TextField()
    Rimage=models.ImageField(upload_to="RecipeImages")
    # new
    Recipe_view_count= models.IntegerField(default=1)

    objects= models.Manager()

    #for better formatting in python shell 
    def __str__(self) -> str:
        return self.Rname 

# class Students(models.Model):
#     student_id = models.OneToOneField(
#         # StudentID,
#           related_name="studentid", 
#           on_delete=models.CASCADE)
    
#     student_name = models.CharField(max_length=100),
#     student_email = models.EmailField(unique=True),
#     student_section = models.CharField(max_length=5),
#     student_age = models.IntegerField(default= 16)
#     student_address = models.TextField()

#     def __str__(self) -> str:
#         return self.student_name


    # class Meta:
    #       ordering:['student_name']
    #       verbose_name: "student"




