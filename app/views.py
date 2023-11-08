from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jampandu(request):
    return HttpResponse('Hi jampandu how are you')
def jigelrani(request):
    return HttpResponse('IAM FINE,HOW ARE YOU')