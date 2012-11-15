# -*- coding: utf8 -*-
from django.http import HttpResponse
from django_telepay.conf import *
from django_telepay.helpers import get_error
from lxml import etree
import django_telepay.requests as telepay_requests


def telepay(request):
    if TELEPAY_CHECK_CERT:
        expected_value = TELEPAY_CERT_VALUE
        value = request.META.get(TELEPAY_CERT_KEY)
        if value != expected_value:
            response_text = '<error>Invalid client SSL certificate</error>'
            return HttpResponse(response_text, mimetype='text/xml', status=403)
    # everything is OK below
    body = request.raw_post_data
    response_text = None
    for request_type in telepay_requests.__all__:
        part = '<%s ' % request_type
        if part in body and '<request>' in body:
            try:
                xml_tree = etree.fromstring(body)
            except etree.XMLSyntaxError, e:
                response_text = get_error(u'XML Error: %s' % e)
            else:
                response_func = getattr(telepay_requests, request_type)
                response_text = response_func(xml_tree)
    if not response_text:
        response_text = get_error(
            u'Not found verify, payment or status tag in request. Stopped'
        )
    return HttpResponse(response_text, mimetype='text/xml')
