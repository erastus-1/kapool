from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns=[

    path('login',views.login,name ='login'),
    path('',views.landing,name = 'landing'),
    path('user/profile',views.pprofile, name = 'profile'),
    path('user/destination',views.pdestination, name = 'destination'),
    path('user/contact',views.pcontact, name = 'contact'),
    path('about',views.about, name = 'about'),
    path('logout',views.logout,name ='logout'),
]