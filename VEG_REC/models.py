from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    # id=models.AutoField()
   # This line of code is defining a ForeignKey field named `user` in the `Recipe` model.
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Rname=models.CharField(max_length=120)
    description=models.TextField()
    Rimage=models.ImageField(upload_to="RecipeImages")
    Recipe_view_count= models.IntegerField(default=1)

    # The line `objects = models.Manager()` in the `Recipe` model is creating a default manager for
    # the model. By defining this line, you are explicitly telling Django to use the `Manager` class
    # provided by Django for managing instances of the `Recipe` model. This manager provides methods
    # for querying and working with instances of the model.
    objects= models.Manager()

    #for better formatting in python shell 
    def __str__(self) -> str:
        return self.Rname 