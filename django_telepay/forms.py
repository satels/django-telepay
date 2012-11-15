# -*- coding: utf8 -*-
from dateutil import parser
from django import forms
from django.conf import settings
from django_telepay import conf
from django_telepay.models import Payment
import pytz


class _FormWithCodeErrors(object):

    CODE_CHOICES = []

    def get_code(self):
        if not self.errors:
            return 0
        code_choices = getattr(self, 'CODE_CHOICES', [])
        for key, code in code_choices:
            if key in self.errors:
                return code
        return 2


class VerifyForm(forms.ModelForm, _FormWithCodeErrors):

    class Meta:
        model = Payment
        fields = ('service', 'account')

    def clean_service(self):
        service = self.cleaned_data['service']
        if service != conf.TELEPAY_SERVICE_ID:
            raise forms.ValidationError(u'Service number is incorrect')
        return service


class PaymentForm(VerifyForm):

    date = forms.CharField()
    sum = forms.IntegerField(min_value=1)

    class Meta:
        model = Payment
        exclude = ('code',)

    def clean_date(self):
        date = self.cleaned_data['date']
        try:
            date = parser.parse(date)
        except ValueError:
            raise forms.ValidationError(u'Error in date value')
        else:
            date = date.replace(tzinfo=None)
        return date

    def clean_id(self):
        id = self.cleaned_data['id']
        if Payment.objects.filter(id=id):
            raise forms.ValidationError(u'Payment with id %s already exists' % id)
        return id

    def clean_sum(self):
        sum = self.cleaned_data['sum']
        sum = float(sum)/100
        return sum


class StatusForm(forms.Form, _FormWithCodeErrors):

    id = forms.IntegerField()

    CODE_CHOICES = [
        ('id', 15),
    ]

    def clean_id(self):
        id = self.cleaned_data['id']
        if not Payment.objects.filter(id=id):
            raise forms.ValidationError(u'Payment with id %s not found' % id)
        return id
