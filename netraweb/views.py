from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request,"index.html")

    

def change_det(request):
  return render(request,"change_det.html")

def fea_ext(request):
  return render(request,"fea_ext.html")

def loader(request):
  return render(request,"loader.html")

<<<<<<< HEAD
def new_login(request):
  return render(request,"new_login.html")
=======
def change_detected_result(request):
  return render(request,"change_detected_result.html")
>>>>>>> 6b5660382ed0797fed8a9d7d3750e2648eb5237c

def change_detection(request):

    
        for file in request.FILES.getlist('myfile'):
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                print("##3",filename)
        
        for file in request.FILES.getlist('myfile2'):
                fs2 = FileSystemStorage()
                filename2 = fs2.save(file.name, file)
                print("##3",filename2)
        
    
        return render(request,"change_det.html")  
        


def feature_extraction(request):

    
        for file in request.FILES.getlist('fmyfile'):
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                print("##3",filename)
        

        
    
        return render(request,"fea_ext.html")  
        


def login(request):  
    return render(request,"login.html")  
