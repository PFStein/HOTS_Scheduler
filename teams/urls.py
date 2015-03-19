'''
Created on Mar 19, 2015

@author: pstein
'''

from django.conf.urls import patterns, url

from teams import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)


#     url(r'^(?P<pk>\w{3,50})/$', views.TeamDetailView.as_view(),
#         name='team_detail'),
#     url(r'^(?P<pk>\w{3,50})/$', views.PlayerDetailView.as_view(),
#          name='player_detail'),