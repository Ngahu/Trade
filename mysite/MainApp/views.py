from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.template import loader

def index(request):
    template = loader.get_template('MainApp/index.html')

    return HttpResponse(template.render(request))

