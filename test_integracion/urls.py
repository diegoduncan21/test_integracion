from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from test_integracion.api import PersonResource

entry_resource = PersonResource()

urlpatterns = patterns('',
    url(r'^$', 'test_integracion.views.index', name='index'),
)
