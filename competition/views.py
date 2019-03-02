from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
def index(request):
    return HttpResponse("Competitons page")

def active(request):
    return HttpResponse("This are active competitions")

def planned(request):
    return HttpResponse("This are planned competitions")

def history(request):
    return HttpResponse("This is competitions history")