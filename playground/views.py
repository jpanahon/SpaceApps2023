from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(req):
    return render(req, 'index.html')
    #return render(req, 'index.html')