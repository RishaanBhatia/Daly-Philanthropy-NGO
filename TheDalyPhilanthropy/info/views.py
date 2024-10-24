from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def home(request):
    return render(request, 'index.html', {})

def home2(request):
    return render(request, 'index.html', {})

# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def mission(request):
    return render(request, 'mission.html')