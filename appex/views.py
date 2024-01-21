from django.shortcuts import render

# Create your views here.

def index(request):
    services = ['web design', 'web developer', 'product management', 'app development']
    return render(request, 'index.html', {"services": services})

def counter(request):
    words = request.POST.get("content")
    num_of_words = len(words.split())
    return render(request, 'count.html', {"content": num_of_words})


def register(request):
    
    return render(request, 'register.html')

