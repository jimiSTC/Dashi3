from django.shortcuts import render
from .sqlPlugin import Dashi2, Donation
#from .live import Dashi2
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from tabulate import tabulate


from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

html = 'Welcome to the DashiKombu index page' + '<p> For the Dashi Dashboard </p> <a href="http://127.0.0.1:8000/dashikombu/dashiboard">Click here</a>'

def index(request):
    return HttpResponse(html)

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def DashiBoard(request):
    print("test.....................dashi...view")
    SalesResults = Dashi2()
    DonationResults = Donation()
    template = loader.get_template('Dashi.html')
    context = {
        'SalesResults': SalesResults,
        'DonationResults': DonationResults
    }
    print(context)
    return HttpResponse(template.render(context, request))