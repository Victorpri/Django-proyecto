from django.shortcuts import render
from django.template import Template, Context
from django.template import loader


# Create your views here.

def inicio(request):
    return render(request, 'index.html')
