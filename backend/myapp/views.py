from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

# Create your views here.

def movies(request):
    if(request.method=='GET'):
        return JsonResponse({"hello":"movies"})

def characters(request):
    if(request.method=='GET'):
        return JsonResponse({"hello":"characters"})