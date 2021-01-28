from .forms import *
from .models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View."""


def home(request):
    date = dt.date.today()

    return render(request, 'index.html',locals())


def profile(request):
    current_user = request.user

    return render(request, 'user/profile.html',locals())

def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.user = current_user
            add.save()
        return redirect('user/update.html')

    else: 
        form = UpdateForm()
    return render(request, '/',{'form':form})


@login_required(login_url='/accounts/login/')
def destination(request):
    return render(request, '/')


@login_required(login_url='/accounts/login/')
def contact(request):
    return render(request, '/')


@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, '/')


