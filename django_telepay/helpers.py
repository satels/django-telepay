# -*- coding: utf8 -*-


def get_error(error_text):
    return '<error>%s</error>' % error_text


def get_result(data):
    attr_text = ' '.join('%s="%s"' % item for item in data.items())
    text = '<result %s/>' % attr_text
    return text


def get_response(response_text):
    return '<response>%s</response>' % response_text