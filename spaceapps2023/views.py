from django.shortcuts import render
from django.http import HttpResponse
import psutil
import subprocess

def home(req):
    return render(req, 'index.html')

def about_page(req):
    return render(req, 'about.html')

def map_page(req):
    return render(req, 'map.html')

def app_integration(req):
    subprocess.Popen(["streamlit", "run", "src/app.py"])
#     proc.wait()

# # Get the process details using psutil
#     process = psutil.Process(proc.pid)

#     # Get the list of network connections for the process
#     connections = process.connections(kind="inet")

#     # Extract the IP address from the connections
#     ip_address = connections[0].laddr.ip  # Assuming the first connection contains the IP address

    # print("IP Address:", ip_address)

    return HttpResponse("app is running")
    

def app4a_integration(req):
    subprocess.Popen(["streamlit", "run", "app4a.py"])
#     proc.wait()

# # Get the process details using psutil
#     process = psutil.Process(proc.pid)

#     # Get the list of network connections for the process
#     connections = process.connections(kind="inet")

#     # Extract the IP address from the connections
#     ip_address = connections[0].laddr.ip  # Assuming the first connection contains the IP address

    # print("IP Address:", ip_address)

    return HttpResponse("app4a is running")