from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from . import views

urlpatterns=[

    url('login',views.login,name ='login'),
    url('',views.landing,name = 'landing'),
    url('user/profile',views.pprofile, name = 'profile'),
    url('update/',views.profile_update, name='update'),
    url('user/destination',views.pdestination, name = 'destination'),
    url('user/contact',views.pcontact, name = 'contact'),
    url('about',views.about, name = 'about'),
    url('logout',views.logout,name ='logout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
