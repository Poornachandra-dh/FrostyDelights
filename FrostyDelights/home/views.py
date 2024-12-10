from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context =  {
        "variable": "this is sent"
    }
    return render(request ,'index.html',context)
   # return HttpResponse("this is homepage page")
@login_required(login_url='login')
def about(request):
    return render(request ,'about.html')
    #return HttpResponse("this is about page")
@login_required(login_url='login')
def services(request):
    return render(request ,'services.html')
    #return HttpResponse("this is services page")
@login_required(login_url='login')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name , email=email , message=message , date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent !')

    return render(request ,'contact.html')
    #return HttpResponse("this is contact page")

def custom(request):
   return render(request ,'custom.html')



#@login_required(login_url='login')
#def HomePage(request):
 #   return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'home/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("name or Password is incorrect!!!")

    return render (request,'templates/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')








