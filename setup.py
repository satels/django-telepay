#!/usr/bin/env python
#coding: utf-8
from distutils.core import setup

import sys
reload(sys).setdefaultencoding("UTF-8")

setup(
    name='django-telepay',
    version='0.0.0',
    author='Ivan Petukhov, NetAngels',
    author_email='satels@gmail.com, info@netangels.ru',
    packages=['django_telepay', 'django_telepay.backends'],
    url='http://netangels.ru/',
    download_url = 'http://netangels.ru',
    license = 'MIT license',
    description = u'Приложение для работы с telepay.'.encode('utf8'),
    long_description = open('README.rst').read().decode('utf8'),

    classifiers=(
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
