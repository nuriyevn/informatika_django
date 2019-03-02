from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# Create your views here.

def index(request):
    return HttpResponse("This is overall page")

def about(request):
    return HttpResponse("This is about page")

def news(request):
    return HttpResponse("This is news page")

def blogs(request):
    return HttpResponse("This is blogs page")

def discussions(request):
    return HttpResponse("This is discussions page")

def help(request):
    return HttpResponse("This is help page")

def resource(request):
    return HttpResponse("This is resource page")

def contact(request):
    return HttpResponse ("This is contact page")