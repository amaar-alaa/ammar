from django.db import models

# Create your models here.
class Image1(models.Model):
   Photo=models.ImageField() 
   def __str__(self):
        return 'الصورة الرئيسية '

    
class Image2(models.Model):
   Photo=models.ImageField() 
   def __str__(self):
        return 'about image'

class Image3(models.Model):
   Photo=models.ImageField() 
   def __str__(self):
        return 'skill image '

class Image4(models.Model):
   Photo=models.ImageField() 
   def __str__(self):
        return 'performance images '

            

    
    