#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals


from ssllabs.object import Object

class HstsPolicy(Object):
    '''The HSTS Policy, accessed from
    :meth:`ssllabs.endpointdetails.EndpointDetails.hstsPolicy`'''
    def __init__(self, data):
        self.__LONG_MAX_AGE = data.get('LONG_MAX_AGE')
        self.__header = data.get('header')
        self.__status = data.get('status')
        self.__error = data.get('error')
        self.__maxAge = data.get('maxAge')
        self.__includeSubDomains = data.get('includeSubDomains')
        self.__preload = data.get('preload')
        self.__directives = data.get('directives')

    @property
    def LONG_MAX_AGE(self):
        '''this constant contains what SSL Labs considers to be
        sufficiently large max-age value'''
        return self.__LONG_MAX_AGE

    @property
    def header(self):
        '''the contents of the HSTS response header, if present'''
        return self.__header

    @property
    def status(self):
        '''HSTS status:

        unknown
            either before the server is checked or when its HTTP response headers are not available
        absent
            header not present
        present
            header present and syntatically correct
        invalid
            header present, but couldn't be parsed
        disabled
            header present and syntatically correct, but HSTS is disabled
        '''
        return self.__status

    @property
    def error(self):
        '''error message when error is encountered, null otherwise'''
        return self.__error

    @property
    def maxAge(self):
        '''the max-age value specified in the policy; null if policy is
        missing or invalid or on parsing error; the maximum value currently
        supported is 9223372036854775807'''
        return self.__maxAge

    @property
    def includeSubDomains(self):
        '''true if the includeSubDomains directive is set; null
        otherwise'''
        return self.__includeSubDomains

    @property
    def preload(self):
        '''true if the preload directive is set; null otherwise'''
        return self.__preload

    @property
    def directives(self):
        '''list of raw policy directives'''
        return self.__directives
