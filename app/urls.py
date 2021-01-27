from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url('login',views.login,name ='login'),
    url('profile/',views.profile_info, name='profile'),
    url('update/',views.profile_update, name='update'),
    url('driver/destination',views.destination, name = 'destination'),
    url('driver/contact',views.contact, name = 'contact'),
    url('about',views.about, name = 'about'),
    url('logout',views.logout,name ='logout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

