from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.utils.translation import ugettext as _
import locale
import gettext

import os

#locale.setlocale(locale.LC_ALL, 'de.UTF-8')

# Create your views here.
def index3(request):
    # locale.setlocale(locale.LC_ALL,  ('uk_UA', 'UTF-8'))
    # siteTitle = _("Login")
    # return HttpResponse( _("Login"))
    context = {
        'site_title': 'sdf'
    }
    # import locale
    # import gettext
    os.environ['LANGUAGE'] = 'uk_UA'
    gettext.bindtextdomain('django', settings.LOCALE_PATHS[0])
    gettext.textdomain('django')
    print(gettext.gettext('Login'))
    return HttpResponse( gettext.gettext('Login'))

def index(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return HttpResponse(dir_path)