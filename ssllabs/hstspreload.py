#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.object import Object
from ssllabs.util import objectornone

class HstsPreload(Object):
    '''The HSTS Preload, accessed from
    :meth:`ssllabs.endpointdetails.EndpointDetails.hstsPreload`.

    The HstsPreload object contains preload HSTS status of one source for the
    current hostname. Preload checks are done for the current hostname, not for
    a domain name. For example, a hostname "www.example.com" tested in SSL Labs
    would come back as "present" if there is an entry for "example.com" with
    includeSubDomains enabled or if there is an explicit entry for
    "www.example.com".
    '''
    def __init__(self, data):
        self.__source = data.get('source')
        self.__status = data.get('status')
        self.__error = data.get('error')
        self.__sourceTime = (datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['sourceTime'])) if 'sourceTime' in data else None

    @property
    def source(self):
        '''source name'''
        return self.__source

    @property
    def status(self):
        '''preload status:
            
        * error
        * unknown - either before the preload status is checked, or if the information is not available for some reason.
        * absent
        * present
        '''
        return self.__status

    @property
    def error(self):
        '''error message, when status is "error"'''
        return self.__error

    @property
    def sourceTime(self):
        '''datetime, when the preload database was retrieved'''
        return self.__sourceTime
