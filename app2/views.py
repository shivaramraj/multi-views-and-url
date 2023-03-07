from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def power_star(request):
    return HttpResponse('<h1>Manalni evadra apedhi</h1>')

def janasena(request):
    return HttpResponse('<h3> vote for janasena</h3>')