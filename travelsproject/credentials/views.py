from collections import UserDict
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user1=auth.authenticate(username=username,password=password)


        if user1 is not None:
            auth.login(request,user1)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render (request,"login.html")


def register(request):
   
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email_id']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                 user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                 user.save();
                 print("user createrd")
                 return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect(request,'register')
        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

