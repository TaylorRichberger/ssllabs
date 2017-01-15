#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import timedelta
import six

from ssllabs.object import Object

class Protocol(Object):
    '''A supported protocol, accessed through
    :meth:`ssllabs.endpointdetails.EndpointDetails.protocols`'''
    def __init__(self, data):
        self.__id = data.get('id')
        self.__name = data.get('name')
        self.__version = data.get('version')
        self.__v2SuitesDisabled = data.get('v2SuitesDisabled')
        self.__q = data.get('q')
    @property
    def id(self):
        '''protocol version number, e.g. 0x0303 for TLS 1.2'''
        return self.__id
    @property
    def name(self):
        '''protocol name, i.e. SSL or TLS.'''
        return self.__name
    @property
    def version(self):
        '''protocol version, e.g. 1.2 (for TLS)'''
        return self.__version
    @property
    def v2SuitesDisabled(self):
        '''some servers have SSLv2 protocol enabled, but with all SSLv2 cipher
        suites disabled. In that case, this field is set to true.'''
        return self.__v2SuitesDisabled
    @property
    def q(self):
        '''0 if the protocol is insecure, null otherwise'''
        return self.__q
