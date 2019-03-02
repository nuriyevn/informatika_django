from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
#from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Task page")
def all(request):
    return HttpResponse("This is all your tasks")

def statistics(request):
    return HttpResponse("This is statistics page")

def results(request):
    return HttpResponse("This is result page")