from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from test_integracion.api import PersonResource

entry_resource = PersonResource()

urlpatterns = patterns('',
    url(r'^api/', include(entry_resource.urls)),

    url(r'^', include('test_integracion.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
