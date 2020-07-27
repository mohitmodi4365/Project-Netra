from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import change_d
import cv2
from PIL import Image
import numpy as np
from cv2 import cv2
import os
from netra.settings import MEDIA_ROOT
import base64
# i1=""
# i2=""
# file1=""
# file2=""
# beforeimagename=""
# afterimagename=""
# afterimagename_wo_ext=""
# beforeimagename_wo_ext=""
# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):  
    return render(request,"login.html")      

def change_det(request):
  return render(request,"change_det.html")

def fea_ext(request):
  return render(request,"fea_ext.html")

def loader(request):
  return render(request,"loader.html")

def change_detection_result(request,i1,i2,file1,file2):
        
        render(request,"change_detection_result.html")
  
def new_login(request):
  return render(request,"new_login.html")


def change_detection(request):

    
        for file in request.FILES.getlist('myfile'):
                fs = FileSystemStorage()
                file1=file.name
                filename = fs.save(file.name, file)
                f1=os.path.abspath(os.path.join(MEDIA_ROOT, file1))


        i1 = change_d()
        i1.img=filename
        print(filename)
        print(file1)
        print(i1)
        
        for file in request.FILES.getlist('myfile2'):
                fs2 = FileSystemStorage()
                file2=file.name
                filename2 = fs2.save(file.name, file)
                f2=os.path.abspath(os.path.join(MEDIA_ROOT, file2))

        i2 = change_d()
        i2.img=filename2
        print(os.path.splitext(file1)[0])
        beforeimagename_wo_ext=os.path.splitext(file1)[0]
        afterimagename_wo_ext=os.path.splitext(file2)[0]
      
        beforeimagename=beforeimagename_wo_ext+'.jpg'
        afterimagename=afterimagename_wo_ext+'.jpg'

        
        print("@")
        diff_in_image=changedetection(beforeimagename,afterimagename_wo_ext)
        print("@@")

        next=reversefoto(diff_in_image)
        print("@@@")

# diffimage2='nextdiff in india pak after (960 x 540).png'
        next2=reversefotoa(next)
        print("@@@@")

# afterimagename2='india pak after (960 x 540).jpg'
        merge(afterimagename, 'F&F '+afterimagename_wo_ext+'.png',next2, position=(0,0))
        print("@@@@@")

        i3 = change_d()
        i3.img='F&F '+afterimagename_wo_ext+'.png'

        return render(request,"change_detection_result.html",{'i1':i1,'i2':i2,'i3':i3})

        # return change_detection_result(request,i1,i2,file1,file2)
        # return (request,"/change_detection_result",{'i1' : i1,'i2' : i2,'file1' : file1,'file2':file2})  
        


def feature_extraction(request):

    
        for file in request.FILES.getlist('fmyfile'):
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                print("##3444",filename)

        print(filename)
        
        response = str(base64.b64encode(open(filename,'rb').read()))
        response=response[2:]
        print(response)


        
    
        return render(request,"fea_ext.html")  
        





def reversefoto(diffimage):
  img = Image.open(diffimage)
  img = img.convert("RGBA")
  datas = img.getdata()

  newData = []
  for item in datas:
      if item[0] == 255 and item[1] == 0 and item[2] == 0:
          # newData.append((255, 255, 255, 0))
          newData.append(item)
      else:
          newData.append((255, 255, 255, 0))
          # newData.append((255, 0, 0, 255))
        
  img.putdata(newData)
  img.save('next'+diffimage, "PNG")

  return 'next'+diffimage


def merge(input_image_path,output_image_path,png_image_path,position):
    img=os.path.abspath(os.path.join(MEDIA_ROOT, input_image_path))
    base_image = Image.open(img)
    png = Image.open(png_image_path)
    width, height = base_image.size

    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    transparent.paste(base_image, (0,0))
    transparent.paste(png, position, mask=png)
    transparent.show() #to pop up changed detected image.
    transparent.save('media/'+output_image_path)

def changedetection(beforeimagename,afterimagename_wo_ext):
  f1=os.path.abspath(os.path.join(MEDIA_ROOT, beforeimagename))

  image1 = cv2.imread(f1)
  f2=os.path.abspath(os.path.join(MEDIA_ROOT, afterimagename_wo_ext+".jpg"))
  
  image2 = cv2.imread(f2)
  # image1 = cv2.imread(beforeimagename)
  # image2 = cv2.imread(afterimagename_wo_ext+".jpg")
  # image1 = cv2.resize(image11, (480, 270)) 
  # image2 = cv2.resize(image21, (480, 270))  


  difference = cv2.absdiff(image1, image2)
  # color the mask red
  Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
  ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)

  difference[mask != 255] = [0, 0, 255]

  image1[mask != 255] = [0, 0, 255]
  image2[mask != 255] = [0, 0, 255]

  boundingBox = 10
  percent = 20

  rows, cols = (image1.shape[0]-boundingBox,image2.shape[1]-boundingBox) 
  for k in range(boundingBox,rows-boundingBox):#pixel
      for l in range(boundingBox,cols-boundingBox):#reddot
          if(difference[k][l][2] == 255):
              x=k-boundingBox
              y=l-boundingBox
              count = 0
              flg = False
              count2 = boundingBox*boundingBox*4
              for i in range(0,boundingBox*2):#boundbox
                  for j in range(0,boundingBox*2):#boundbox
                      if(difference[x+i][y+j][2] == 255):
                          count += 1

                          if(((count * 100) / count2) > percent):#percentage
                              flg = True
                              break

              if(flg == False):
                  for i in range(0,boundingBox*2):
                      for j in range(0,boundingBox*2):
                          difference[x+i][y+j][2] = 0
                          

  # cv2.imwrite('change in ' + beforeimagename, image1)
  # cv2.imwrite('change in ' + afterimagename, image2)
  # difference1 = cv2.resize(difference,(1920,1080))
  cv2.imwrite('media/diff in ' + afterimagename_wo_ext+'.png', difference)
  cv2.imwrite('diff in ' + afterimagename_wo_ext+'.png', difference)

  # fs=FileSystemStorage()
  # filename = fs.save(afterimagename_wo_ext+'.png', difference)
  return 'diff in ' + afterimagename_wo_ext+'.png'


def reversefotoa(diffimage):
  img = Image.open(diffimage)
  img = img.convert("RGBA")
  datas = img.getdata()

  newData = []
  for item in datas:
      if item[0] == 255 and item[1] == 0 and item[2] == 0:
          newData.append((255, 0, 0, 99))
         
      else:
          newData.append((255, 255, 255, 0))
        
        
  img.putdata(newData)
  img.save('just'+diffimage, "PNG")

  return 'just'+diffimage

