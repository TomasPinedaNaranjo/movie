from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    return render(request, 'home.html', {'name': 'Greg Lim'})
    #return render(request, 'home.html')
    #return HttpResponse('<h1>Welcome to Home page</h1>')




