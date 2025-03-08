from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Recipe(models.Model):
    # id=models.AutoField()
   # This line of code is defining a ForeignKey field named `user` in the `Recipe` model.
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Rname=models.CharField(max_length=120)
    description=models.TextField()
    Rimage=models.ImageField(upload_to="RecipeImages")
    # new
    Recipe_view_count= models.IntegerField(default=1)

    # The line `objects = models.Manager()` in the `Recipe` model is creating a default manager for
    # the model. By defining this line, you are explicitly telling Django to use the `Manager` class
    # provided by Django for managing instances of the `Recipe` model. This manager provides methods
    # for querying and working with instances of the model.
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




