from django.db import models


class change_d():  
    img = str
 

class user(models.Model):  
    fullname            = models.CharField(max_length=50,unique=True) 
    email_id               = models.CharField(max_length=100,null=True,unique=True)
    password            = models.CharField(max_length=100,null=True)
    user_type              = models.CharField(max_length=100,null=True)
    user_status              = models.CharField(max_length=100,null=True)
   