from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signupCoach/', views.signupCoach, name='signupCoach'),
    url(r'^signupPlayer/', views.signupPlayer, name='signupPlayer'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^playerProfile/', views.playerProfile, name='playerProfile'),
    url(r'^exploreCoach/', views.exploreCoach, name='exploreCoach'),
    url(r'^explorePlayer/', views.explorePlayer, name='explorePlayer')
]