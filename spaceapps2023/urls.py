"""
URL configuration for spaceapps2023 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from spaceapps2023.views import home
from spaceapps2023.views import about_page
from spaceapps2023.views import map_page
from spaceapps2023.views import streamlit_integration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index.html', home, name='home'),
    path('about.html', about_page, name='about'),
    path('map.html', map_page, name = 'map'),
    path('streamlit_integration.html', streamlit_integration, name='app4a')
]
