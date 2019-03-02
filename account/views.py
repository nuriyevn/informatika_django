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

# This is reqistration view
def register(request):
    return HttpResponse("This is registration page")

# This is login view
def login_user_bla(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/account/dashboard')

    form = LoginForm(request.POST or None)
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # apartments = Apartment.object.filter(user=request.user)
                # return render(request, 'apartment/index.html', {'apartments': apartments})
                return HttpResponseRedirect('/apartment/index')
            else:
                return render(request, 'profile/login.html', {"error_message": "Your account has been disabled"})
        else:
            return render(request, 'profile/login.html', {"error_message": "Invalid login"})
    context = {
        "form": form,
    }
    return render(request, 'profile/login.html', context)


#This is logout view
def logout_user(request):
    return  HttpResponse("This is logout page")

#This is dashboard view
def dashboard(request):
    return  HttpResponse("This is your dashboard")
