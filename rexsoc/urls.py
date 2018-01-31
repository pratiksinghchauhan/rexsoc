"""rexsoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views
from . import settings
from log.forms import loginform
from log.views import signup
from log.views import about
from accounts.views import userhome,reviewview,submitreview,blog,profilesettings,you,emailsettings,passwordsettings,picuploadsettings,searchresults,someone

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('log.urls')),
    url(r'^rexsoc/$', signup), 
    url(r'^about/$', about),  
    url(r'^signup/$', signup),  
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': loginform,'redirect_field_name':'/userhome/'}),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),  
    url(r'^success/$', views.login, {'template_name': 'login.html', 'authentication_form': loginform,'redirect_field_name':'/userhome/'}),  
    url(r'^userhome/$', userhome), 
    url(r'^review/$', reviewview), 
    url(r'^submitreview/$', submitreview),
    url(r'^blog/$', blog), 
    url(r'^accountsettings/$', profilesettings),
    url(r'^emailsettings/$', emailsettings), 
    url(r'^passwordsettings/$', passwordsettings),   
    url(r'^profile/$', you), 
    url(r'^upload/$', picuploadsettings),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^profile/(.*)$', someone),
    url(r'^searchresults/$',searchresults),
]
