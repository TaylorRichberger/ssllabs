#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from ssllabs.object import Object

class HpkpPolicy(Object):
    '''The HPKP Policy, accessed from
    :meth:`ssllabs.endpointdetails.EndpointDetails.hpkpPolicy` and
    :meth:`ssllabs.endpointdetails.EndpointDetails.hpkpRoPolicy`'''
    def __init__(self, data):
        self.__status = data.get('status')
        self.__header = data.get('header')
        self.__error = data.get('error')
        self.__maxAge = data.get('maxAge')
        self.__includeSubDomains = data.get('includeSubDomains')
        self.__reportUri = data.get('reportUri')
        self.__pins = data.get('pins')
        self.__matchedPins = data.get('matchedPins')
        self.__directives = data.get('directives')

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
    def header(self):
        '''the contents of the HSTS response header, if present'''
        return self.__header


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
    def reportUri(self):
        '''the report-uri value from the policy'''
        return self.__reportUri

    @property
    def pins(self):
        '''list of all pins used by the policy'''
        return self.__pins

    @property
    def matchedPins(self):
        '''list of pins that match the current configuration; each list entry
        contains a :class:`dict` with two fields, hashFunction and value
        (hex-encoded)'''
        return self.__matchedPins

    @property
    def directives(self):
        '''list of raw policy directives (name-value pairs)'''
        return self.__directives
