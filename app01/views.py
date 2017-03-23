'''
default views
'''
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    '''
    index handle
    '''
    return HttpResponse("Hello, world. You're at the polls index")
