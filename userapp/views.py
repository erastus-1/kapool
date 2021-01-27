from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, '/')


@login_required(login_url="/accounts/login/")
def profile(request):
    return render(request, '/')


@login_required(login_url='/accounts/login/')
def destination(request):
    return render(request, '/')


@login_required(login_url='/accounts/login/')
def contact(request):
    return render(request, '/')


@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, '/')


