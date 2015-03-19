'''
Created on Mar 19, 2015

@author: pstein
'''

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from teams import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    (r'^about/', TemplateView.as_view(template_name="about.html"))
)