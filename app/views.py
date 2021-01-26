from .forms import *
from .models import *
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    projects = Projects.objects.all()

    return render(request,'all/home.html',locals())

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
        return redirect('profile')

    else: 
        form = UpdateForm()
    return render(request, '/',{'form':form})

@login_required(login_url='/accounts/login/')
def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        message = f'{search_term}'
        profile_pic = User.objects.all()

        return render(request,'/',locals())

    return redirect('/')

