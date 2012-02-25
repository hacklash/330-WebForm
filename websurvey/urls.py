from django.conf.urls.defaults import patterns, include, url
from survey.forms import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^survey/$', SurveyWizard([ControllerForm, GateForm, ScrollingForm,
                                 HGameForm, VDeveloperForm, VCaveForm, VTreasureForm])),
    # Examples:
    url(r'^$', 'websurvey.views.home', name='home'),
    url(r'^websurvey/', include('websurvey.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'$', 'survey.views.index'),
)
