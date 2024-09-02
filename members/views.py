from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Home(requests):
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
    return render(requests, 'myfirst.html')
