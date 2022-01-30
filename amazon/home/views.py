from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def home(request):
    return HttpResponse(
    "<nav>"
    "<a href='contactus'>contactus</a> <a href='http://127.0.0.1:8000/'>home</a> <a href='about'>about</a><br>"
    "</nav>"
    "<br>"
    "Hello"
    )

# Create your views here.
