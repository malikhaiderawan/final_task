

from urllib import request
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

from django.contrib.auth.decorators import login_required
from .decorators import admin_only, user_only
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import ProfileForm

def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user_orders.html', {'orders': orders})

def profile_management(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_management')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile_management.html', {'form': form})

def order_tracking(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'order_tracking.html', {'order': order})

# Create your views here.
@login_required

def home(request):
    return render(request,'home.html')
@user_only
def register(request):
    #check post method and save values
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        #user authentication
        if User.objects.filter(username=username).exists():
            messages.error(request,'Yours Username alreasy exists please Choose another username.Thank YOU!')
            return render(request, 'register.html')
        #error handling
        if pass1!=pass2:
            messages.error(request,'Both password are not same!Please Enter the Both same Passwords.')
            return redirect('register')

        #create new user
        foz=User.objects.create_user(username,email,pass1)
        foz.first_name=fname
        foz.last_name=lname
        foz.is_superuser = False
        foz.save()
        messages.success(request,'You are successfully registered! Now Please Login!')
        return redirect('home')

    return render(request,'register.html')

def Login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'You are successfully logged in!')
            return redirect('home')

        else:
            messages.error(request,'Perhaps Username or Password incorrect. Or U r not registered! IF uh R not Registered please click on Register button for Registration!')
            return render(request,'login.html')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    messages.success(request,'You have been Successfully Logged Out!')
    return redirect('home')




