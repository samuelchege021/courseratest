from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def homepage(request):
    return HttpResponse("wow this is an <strong>awesome</strong>tutorial")


