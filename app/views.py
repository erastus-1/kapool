from .models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    return render(request, '/')

def logout(request):
        logout(request)
        return redirect(request, '/')


@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()

    return render(request,'base.html',locals())

@login_required(login_url='/accounts/login/')
def profile_info(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()

    return render(request, '/',locals())

@login_required(login_url='/accounts/login/')
def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.user = current_user
            add.save()
        return redirect('/')

    else: 
        form = UpdateForm()
    return render(request, '/',{'form':form})

def about(request):
    return render(request, '/')

def destination(request):
    return render(request, '/')


def contact(request):
    return render(request, '/')