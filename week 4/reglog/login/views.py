
from multiprocessing import context
from django.db.models.query_utils import DeferredAttribute
from telnetlib import LOGOUT
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['cpassword']
        
      
        
        if User.objects.filter(username=username):
            messages.error(request, "Username Already exists! Please try someother Username!")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email Already Registered!")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "User name must be under 10 charecters!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Password Didn't match!")
            return redirect('home')            
            
            
        if not username.isalnum():
            messages.error(request, "Username must be Alfa-Numeric")  
            return redirect('home')        
        
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        
        myuser.save()
        namef=myuser.first_name        
        messages.success(request  , "Your account has been successfully created",{'name':namef})
        
        return redirect('signin')
    
    
    return render(request, "signup.html")

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)
        
            
      
        if user is not None:
            login(request, user)
            fname = User.objects.name           
            
            return render(request, "home.html", {'fname':fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
    return render(request, "signin.html")

def signout(request):
    logout(request)
    print('logout')
    return redirect('home')
     