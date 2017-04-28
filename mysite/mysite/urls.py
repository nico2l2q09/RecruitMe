"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   # url(r'^', auth_views.login, {'template_name': 'index.html'}, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^', include('signup.urls')),
	url(r'^signupPlayer/', include('signup.urls')),
	url(r'^signupCoach/', include('signup.urls')),
	url(r'^profile/', include('signup.urls')),
	url(r'^playerProfile/', include('signup.urls')),
    url(r'^exploreCoach/',  include('signup.urls')),
    url(r'^explorePlayer/',  include('signup.urls')),
	url(r'^admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
