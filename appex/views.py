from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home.html')

def counter(request):
    words = request.POST.get("content")
    num_of_words = len(words.split())
    return render(request, 'count.html', {"content": num_of_words})

