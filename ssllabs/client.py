#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from six.moves.urllib.parse import urlsplit, urlunsplit, urlencode
from time import sleep
import six

import requests

class Client(object):
    def __init__(self, entrypoint='https://api.ssllabs.com/api/v2'):
        self.entrypoint = entrypoint

    @property
    def entrypoint(self):
        return urlunsplit((self.__scheme, self.__netloc, self.__path, '', ''))

    @entrypoint.setter
    def entrypoint(self, value):
        parts = urlsplit(value)
        self.__scheme = parts.scheme
        self.__netloc = parts.netloc
        self.__path = parts.path.rstrip('/')

    def info(self):
        path = '/'.join((self.__path, 'info'))
        url = urlunsplit((self.__scheme, self.__netloc, path, '', ''))
        request = requests.get(url)
        request.raise_for_status()
        return request.json()

    def analyze(self, host, publish=False, all=None, ignoreMismatch=False):
        path = '/'.join((self.__path, 'analyze'))

        # Start the run
        query = {'host': host}
        if publish:
            query['publish'] = 'on'

        if all:
            query['all'] = all

        if ignoreMismatch:
            query['ignoreMismatch'] = 'on'

        startnewquery = {'startNew': 'on'}
        startnewquery.update(query)

        url = urlunsplit((self.__scheme, self.__netloc, path, urlencode(startnewquery), ''))
        request = requests.get(url)
        request.raise_for_status()
        data = request.json()

        url = urlunsplit((self.__scheme, self.__netloc, path, urlencode(query), ''))
        while data['status'] in {'IN_PROGRESS', 'DNS'}:
            sleep(10)
            request = requests.get(url)
            request.raise_for_status()
            data = request.json()

        return data
