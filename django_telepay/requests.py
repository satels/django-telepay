# -*- coding: utf8 -*-
from django_telepay import conf
from django_telepay.backends import get_backend
from django_telepay.forms import VerifyForm, PaymentForm, StatusForm
from django_telepay.helpers import get_error, get_response, get_result

__all__ = ('verify', 'payment' , 'status',)


_backend = get_backend(conf.TELEPAY_BACKEND)


def verify(xml_tree):
    tags = xml_tree.xpath("/request/verify")
    if len(tags) != 1:
        return get_error(u'Request must contain exactly one verification element')
    verify_tag = tags[0]
    form = VerifyForm(verify_tag.attrib)
    if form.is_valid():
        form_data = form.cleaned_data
        response_data = _backend.verify(form_data)
    else:
        response_data ={'code': form.get_code()}
    response_text = get_result(response_data)
    response = get_response(response_text)
    return response


def payment(xml_tree):
    tags = xml_tree.xpath("/request/payment")
    if len(tags) < 1:
        return get_error(u'Request must contain one or more payment elements')
    response_text = ''
    for payment_tag in tags:
        data = payment_tag.attrib
        form = PaymentForm(data)
        if form.is_valid():
            form_data = form.cleaned_data
            response_data = _backend.payment(form_data)
            telepay_payment = form.save(commit=False)
            telepay_payment.code = response_data['code']
            telepay_payment.save()
        else:
            id = data['id']
            code = form.get_code()
            response_data = {'id': id, 'code': code, 'final': 0}
        response_text += get_result(response_data)
    response = get_response(response_text)
    return response


def status(xml_tree):
    tags = xml_tree.xpath("/request/status")
    if len(tags) < 1:
        return get_error(u'Request must contain one or more status elements')
    response_text = ''
    for status_tag in tags:
        data = status_tag.attrib
        form = StatusForm(data)
        if form.is_valid():
            form_data = form.cleaned_data
            response_data = _backend.status(form_data)
        else:
            id = data['id']
            code = form.get_code()
            response_data = {'id': id, 'code': code, 'final': 0}
        response_text += get_result(response_data)
    response = get_response(response_text)
    return response
