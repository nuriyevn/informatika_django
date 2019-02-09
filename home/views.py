from django.shortcuts import render, redirect
from django.http import HttpResponse


from urllib import  parse

import gettext
import os
_ = gettext.gettext

def lang(request):
    return render(request, "home/lang.html", {'login': _("Login")})

# Create your views here.
def index3(request):

    return render(request, 'home/home.html')

def index(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return HttpResponse(dir_path)


def change_locale(request, lang):
    p = parse.urlparse(request.META.get('HTTP_REFERER'))

    os.environ['LANGUAGE'] = lang
    if p is not None and p.path != b'':
        return redirect(p.path)
    else:
        return redirect('/admin/')