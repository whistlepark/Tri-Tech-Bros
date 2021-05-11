from django.shortcuts import render

def automation(request):
    return render(request, 'automation.html', context={})
