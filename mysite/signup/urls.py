from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signupCoach/', views.signupCoach, name='signupCoach'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^playerProfile/', views.playerProfile, name='playerProfile')
]