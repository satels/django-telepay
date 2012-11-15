# -*- coding: utf8 -*-


class DefaultBackend(object):
    """
    For all methods:
    input: form_data (example: {'service': 1, 'account': "12345"})
    output: response_data
    (ex.: {'code': '0', 'final': "1", 'trans': "123"})
    """

    def verify(self, form_data):
        raise NotImplementedError

    def payment(self, form_data):
        raise NotImplementedError

    def status(self, form_data):
        raise NotImplementedError