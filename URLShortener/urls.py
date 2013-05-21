from django.conf.urls import patterns, include, url
from shortener.views import urlprocessor, create
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$',create),
	url(r'([^/]+)/([^/]*)',urlprocessor),
)
