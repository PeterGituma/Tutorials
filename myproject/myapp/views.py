from django.shortcuts import render,HttpResponse


def home(request):
    return HttpResponse("Hello, welcome to my Django app!")
# Create your views here.
