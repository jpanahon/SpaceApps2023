from django.shortcuts import render

def home(req):
    return render(req, 'index.html')

def about_page(req):
    return render(req, 'about.html')

def map_page(req):
    return render(req, 'map.html')