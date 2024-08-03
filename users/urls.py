from django.urls import path
from .views import CustomLoginView, profile, dashboard

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
]