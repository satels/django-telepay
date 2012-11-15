# -*- coding: utf8 -*-
from django.conf import settings

TELEPAY_BACKEND = getattr(settings, 'TELEPAY_BACKEND')
TELEPAY_SERVICE_ID = getattr(settings, 'TELEPAY_SERVICE_ID')
TELEPAY_CHECK_CERT =  getattr(settings, 'TELEPAY_CHECK_CERT', True)
TELEPAY_CERT_KEY = getattr(settings, 'TELEPAY_CERT_KEY', None)
TELEPAY_CERT_VALUE = getattr(settings,'TELEPAY_CERT_VALUE', None)
