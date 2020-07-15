from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

    

def change_det(request):
  return render(request,"change_det.html")



def fea_ext(request):
  return render(request,"fea_ext.html")


def login(request):  
    return render(request,"login.html")  
