from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req, 'index.html')

def about_page(req):
    return render(req, 'about.html')

def map_page(req):
    return render(req, 'marine.html')