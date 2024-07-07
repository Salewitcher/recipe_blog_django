from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, Food Lovers!")


def recipes(request):
    return HttpResponse("Hello, Recipes!")