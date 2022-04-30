from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def carrega_login(request):
    return render(request, "login_users/login.html")
