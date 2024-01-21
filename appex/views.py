from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Books

# Create your views here.

def index(request):
    services = ['web design', 'web developer', 'product management', 'app development']
    return render(request, 'index.html', {"services": services})

def counter(request):
    words = request.POST.get("content")
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
                return redirect('home')
        else:
            messages.info(request, 'Password mismatched!')
            return redirect('register')
    else:
        return render(request, 'register.html')

