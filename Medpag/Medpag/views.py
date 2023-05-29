from django.http import HttpResponse
from django.shortcuts import render, redirect
from .templates import *

def prescrip(request):

    return render(request,'/prescripciones.html')
