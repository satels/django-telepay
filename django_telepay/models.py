# -*- coding: utf8 -*-
from django.db import models


class Payment(models.Model):

    id = models.IntegerField(u'Agent Operation ID',
        max_length=8, primary_key=True
    )
    sum = models.FloatField(u'SUM', max_length=4)
    point = models.IntegerField(u'Point number', max_length=4)
    check = models.IntegerField(u'Check number', max_length=4)
    service = models.IntegerField(u'Service number', max_length=4)
    account = models.CharField(u'Customer number', max_length=100)
    date = models.DateTimeField(u'Submit date')
    code = models.IntegerField(u'Code from backend')
