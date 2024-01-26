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
    

    #for better formatting in python shell 
    def __str__(self) -> str:
        return self.Rname 
    