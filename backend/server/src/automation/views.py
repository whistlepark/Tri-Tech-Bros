from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect

def automation(request):
    return HttpResponsePermanentRedirect('http://127.0.0.1:1880/')
    return render(request, 'automation.html', context={})
