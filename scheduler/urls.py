'''
Created on Mar 19, 2015

@author: pstein
'''

from django.conf.urls import patterns, url

from scheduler import views
urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about/', views.AboutView.as_view(),name='about'),
    url(r'^calendar/',views.CalendarView.as_view(), name='calendar'),
    url(r'^teams/',views.TeamIndexView.as_view(),name='teams'),
    url(r'^players/',views.PlayerIndexView.as_view(),name='players'),
    url(r'^teams/(?P<pk>\d+)/$',views.TeamDetailView.as_view(),
        name='team_details'),
    url(r'^players/(?P<pk>\d+)/$',views.PlayerDetailView.as_view(),
        name='player_details'),
)