from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.


# ek template return karvani hai--> the first thing to be done

def recipes(request):
    # Bringing Data from FrontEnd
    if request.method == 'POST': 
       data=request.POST

       Recipe_image = request.FILES.get('Rimage')
       Recipe_name=data.get('Rname')
       Recipe_description= data.get('description')
       print(Recipe_name)
       print(Recipe_description)
       print(Recipe_image)
       
       Recipe.objects.create(
           Rname=Recipe_name,
           description=Recipe_description,
           Rimage=Recipe_image,
       )
       return redirect('/recipes/')#to deal with reload alert problem.(after submission the page url must redirect to the same url)
    queryset=Recipe.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(Rname__icontains = request.GET.get('search'))
        print( request.GET.get('search'))


    context={'page':'Recipes','Recipes':queryset}
    return render(request,'recipes.html',context)

def delete(request, id):
    queryset=Recipe.objects.get(id = id)
    queryset.delete()
    return redirect('/recipes/')
    # return HttpResponse("a")

def update(request, id):
    queryset=Recipe.objects.get(id = id)
    if request.method == 'POST': 
       data=request.POST

       Recipe_image = request.FILES.get('Rimage')
       Recipe_name=data.get('Rname')
       Recipe_description= data.get('description')


       queryset.Rname=Recipe_name
       queryset.description=Recipe_description
       if queryset.Rimage:
          queryset.Rimage=Recipe_image
       queryset.save()
       return redirect('/recipes/')
       
    context={'recipe':queryset}
    return render(request,'update_recipe.html',context)

def login_page(request):
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        data= request.POST
        first_name= data.get('first_name')
        last_name= data.get('last_name')
        username= data.get('username')
        password= data.get('password')

        #Checking if the username already exists-->if yes then showing message of "Username already exists"
        user= User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already exists.")
            return redirect('/register/')
           

        user= User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            # password=password #Not the optimal approach
        )
        #Optimal way to store passwords, also this gets set outside the object.
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully.")


    return render(request, 'register.html')