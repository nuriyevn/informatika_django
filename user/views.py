from django.shortcuts import render

from django.http import HttpResponse

#from django.template import loader

from django.http import Http404

# Create your views here.
def index(request):
    return HttpResponse("Users page")

def all(request):
    return HttpResponse("All users page")

def rating(request):
    return HttpResponse("Users rating")