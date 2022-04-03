#from .models import Forms_one
from email.mime import message
from http.client import HTTPResponse
from django.shortcuts import render,redirect
#from django.contrib.auth.models import user
from .models import Destination
#from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "index.html")

def book(request):
    n=''
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        suggestion=request.POST.get('suggestions','')
        
        if len(name)<0 or len(email)<4 or len(address)<5 or len (suggestion)<5:
            #return HttpResponse('Error !! please Insert Data correctly!!')
            messages.error(request,' plz fill form correctlly!!')
            return redirect("book")
        else:
            eh=Destination(name=name,email=email,address=address,suggestions=suggestion)
            eh.save()
            messages.success(request,'data inserted')
            return redirect("Menu")
    else:
     return render(request, "Book.html")


    ''' if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        Address=request.POST['address']
        suggestions=request.POST['sug']
     destinations=Destination(name=name,email=email,address=Address,suggestions=suggestions)
     destinations.save();
     print('table book successfully!!)'''
    


def menu(request):
    return render(request, "Menu.html")

def gallery(request):
  return render(request, "Gallery.html")
