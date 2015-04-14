# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import ContactFormAjaxView


urlpatterns = patterns('',
    url(r'^$', ContactFormAjaxView.as_view(), name='ajax_form'),
)
