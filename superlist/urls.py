from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'list.views.home_page', name='home'),
    url(r'^lists/', include('list.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
