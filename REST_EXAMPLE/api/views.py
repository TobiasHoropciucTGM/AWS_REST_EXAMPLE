from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def register(request):
    params = {
        "uname": request.GET.get('uname'),
        "email": request.GET.get('email'),
        "password": request.GET.get('password')
    }
    return HttpResponse(params.items())

def test(request):
    return HttpResponse("Test successful")