from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def profile(request):
    return render(request, 'users/profile.html')