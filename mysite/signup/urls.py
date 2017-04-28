from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signupCoach/', views.signupCoach, name='signupCoach'),
    url(r'^signupPlayer/', views.signupPlayer, name='signupPlayer'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<username>\w+$)', views.profile, name='profile'),
    url(r'^playerProfile/', views.playerProfile, name='playerProfile'),
    url(r'^playerProfile/(?P<username>\w+$)', views.playerProfile, name='playerProfile'),
    url(r'^explore/', views.explore, name='explore'),
    #url(r'^explorePlayer/', views.explorePlayer, name='explorePlayer'),
    url(r'^matches/', views.matches, name='matches'),
   # url(r'^matchesCoach/', views.matchesCoach, name='matchesCoach')
]