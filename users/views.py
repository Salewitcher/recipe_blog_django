from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')
