from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):

    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Rname=models.CharField(max_length=120, unique=True)
    description=models.TextField()
    Rimage=models.ImageField(upload_to="RecipeImages")
    Recipe_view_count= models.IntegerField(default=1)


    #for better formatting in python shell 
    def __str__(self) -> str:
        return self.Rname 