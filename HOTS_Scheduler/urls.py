from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HOTS_Scheduler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^scheduler/', include('scheduler.urls', namespace="scheduler")),
    url(r'^admin/', include(admin.site.urls)),
)
