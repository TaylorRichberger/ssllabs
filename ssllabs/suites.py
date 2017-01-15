#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.suite import Suite
from ssllabs.object import Object

class Suites(Object):
    '''Cipher suite collection, accessed from
    :meth:`ssllabs.endpointdetails.EndpointDetails.suites`'''
    def __init__(self, data):
        self.__list = [Suite(suite) for suite in data.get('list', list())]
        self.__preference = data.get('preference')
    @property
    def list(self):
        '''a list of :class:`ssllabs.suite.Suite` objects'''
        return self.__list
    @property
    def preference(self):
        '''true if the server actively selects cipher suites; if null, we were
        not able to determine if the server has a preference'''
        return self.__preference
