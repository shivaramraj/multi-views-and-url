from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def marvel(request):
    return HttpResponse('<h2>this is the first viw of app1</h2>')
def tony_stark(request):
    return HttpResponse('<h1>this is the second viw of app1</h1>')