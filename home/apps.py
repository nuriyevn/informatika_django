from django.apps import AppConfig

class HomeConfig(AppConfig):
    name = 'home'


import gettext
import os
_ = gettext.gettext
from django.conf import settings
from django.utils import translation

# Dictionary of urls that should use special language regardless of language set in browser
#   key = url
#   val = language code
special_cases = {
    '/this/is/some/url/' : 'dk',
    '/his/is/another/special/case' : 'de',
                 }

class LangBasedOnUrlMiddleware(object):
    def process_request(self, request):
        if request.path_info in special_cases:
            lang = 'uk_UA'
            translation.activate(lang)
            request.LANGUAGE_CODE = lang


class LocaleMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not 'LANGUAGE' in os.environ:
            os.environ['LANGUAGE'] = 'az_AZ'

        language_code = os.environ['LANGUAGE']  #TODO, your logic

        translation.activate(language_code)
        gettext.bindtextdomain('django', settings.LOCALE_PATHS[0])
        gettext.textdomain('django')
        response = self.get_response(request)
        translation.deactivate()
        return response