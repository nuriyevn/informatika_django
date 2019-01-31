from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
#from django.template import loader
from django.shortcuts import render
from django.http import Http404

# Create your views here.
def index(request):
    return HttpResponse ("Hello Account")

# Create your views here.
