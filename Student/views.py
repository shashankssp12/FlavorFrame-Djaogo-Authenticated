from django.shortcuts import render

# Create your views here.

def stdRegister(request):
  
#   context={'page':'Recipes','Recipes':queryset}
    return render(request,'stdRegister.html', {'page':'Student'})