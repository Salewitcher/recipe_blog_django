from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def profile(request):
    return render(request, 'users/profile.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')
