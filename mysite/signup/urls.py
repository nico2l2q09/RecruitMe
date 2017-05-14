from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signupCoach/', views.signupCoach, name='signupCoach'),
    url(r'^signupPlayer/', views.signupPlayer, name='signupPlayer'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/(?P<username>\w+$)', views.profile, name='profile'),
    #url(r'^playerProfile/', views.playerProfile, name='playerProfile'),
    #url(r'^playerProfile/(?P<username>\w+$)', views.playerProfile, name='playerProfile'),
    url(r'^explore/', views.explore, name='explore'),
    #url(r'^explorePlayer/', views.explorePlayer, name='explorePlayer'),
    url(r'^matches/', views.matches, name='matches'),
    url(r'^logout/', views.logoutuser, name='logoutuser'),
    url(r'^makeMatch/(?P<username>\w+$)', views.makeMatch, name='makeMatch'),
    url(r'^noInterest/(?P<username>\w+$)', views.noInterest, name='noInterest'),
    url(r'^updateProfile/', views.updateProfile, name='updateProfile'),
    url(r'^interested/', views.interestedInYou, name='interestedInYou'),


   # url(r'^matchesCoach/', views.matchesCoach, name='matchesCoach')
]