from django.shortcuts import render,redirect
from django.http import HttpResponse
from One.settings import EMAIL_HOST_USER
from . import form
from .models import Image1,Image2,Image3,Image4
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.


def index(request):
    image1=Image1.objects.all()
    image2=Image2.objects.all()
    image3=Image3.objects.all()
    image4=Image4.objects.all()


    sub = form.Subscribe()
    return render(request, 'index.html',{'form':sub,'image1':image1,'image2':image2,'image3':image3,'image4':image4})


def subscribe(request):
    sub = form.Subscribe()
    if request.method == 'POST':
        sub = form.Subscribe(request.POST)
        name=str(sub['name'].value())
        subject = 'name: ' +str(sub['name'].value())+' email: '+str(sub['email'].value())
        message = str(sub['message'].value())
       
        send_mail(subject,message, EMAIL_HOST_USER,['amaar.alaa93@gmail.com'], fail_silently = False)
        messages.success(request, 'Your submission has been successful. Thank you')
        return redirect('/')
    else:    
        messages.success(request, 'Some things are not valid, please check and try again')
        return redirect('/')
