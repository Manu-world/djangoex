from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import Book
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def index(request):
    services = ['web design', 'web developer', 'product management', 'app development']
    return render(request, 'index.html', {"services": services})

@login_required
def counter(request):
    words = 'Manu akimidis'
    num_of_words = len(words.split())
    return render(request, 'count.html', {"content": num_of_words})


def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This Email already exists. Try a different one')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password mismatched!')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Looks like you dont have an account yet!')
            return redirect('login')

    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')


def details(request, pk):
    return render(request, 'details.html', {'pk':pk})