from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

def principal(request):  

    doc_externo=loader.get_template('index.html')  #necesitamos importar el loader el cual tengra dentro el get_template (mirar la seccion de templates en settings.py)

    documento=doc_externo.render({})

    return HttpResponse(documento)