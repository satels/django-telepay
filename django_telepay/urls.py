# -*- coding: utf8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('django_telepay.views',
    url(r'^$',  'telepay', name='telepay-telepay'),
)