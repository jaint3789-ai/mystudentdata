from django.shortcuts import render
from django.http import HttpResponse
from django.template import *
from .models import *

# Create your views here.
def first_view(request):
    return HttpResponse("This is the first view.")



def second(request):
    return HttpResponse("This is the second view.")

def send_html_file(request):
    return render(request, 'sample.html')

def send_form(request):
    return render(request, 'tanisha/form.html')

def home_view(request):
    return render(request, 'myhome.html')

def rooms(request):
    return render(request, 'rooms.html')

def myimage(request):
    return render(request, 'image.html')



def student_data(request):
    myname = students.objects.all().values()
    return render(request, 'display.html',context= {'myname': myname})