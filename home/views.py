from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



# def home(request):
#     return HttpResponse("""
#                         <h1>I am coming from Django Server</h1>
#                         <p>lorem34</p>
#                         <br>
#                         <hr>
#                         <p>Hi you are super cool </p>
#                         """)

def home(request):
    people=[
        {'name': 'shashank','age':23},
        {'name': 'charu','age':13} ,
        {'name': 'tashu','age':22},
        {'name': 'Barbie','age':13}
    ]
    text=""" Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat eligendi commodi quod quisquam. Dignissimos nulla doloremque, doloribus temporibus corporis magnam eaque deleniti magni suscipit. Maxime quos necessitatibus inventore facilis vero enim"""
    vegetable=['Potato','Tomato','Ginger','Eggplant']

    #     print(people)
    print(people)
    str="nitis"
    print(str[::-1])
    return render(request,'index.html',context={'page':'Home','people': people,'text':text, 'vegetable':vegetable})

def contact(request):
    context= {'page':'Contact'}
    return render(request,'contact.html',context)

def about(request):
    context= {'page':'About'}
    return render(request, 'about.html',context)


