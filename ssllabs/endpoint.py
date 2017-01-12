#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import timedelta

from ssllabs.endpointdetails import EndpointDetails
from ssllabs.object import Object

class Endpoint(Object):
    def __init__(self, data):
        self.__ipAddress = data.get('ipAddress')
        self.__serverName = data.get('serverName')
        self.__statusMessage = data.get('statusMessage')
        self.__statusDetails = data.get('statusDetails')
        self.__statusDetailsMessage = data.get('statusDetailsMessage')
        self.__grade = data.get('grade')
        self.__gradeTrustIgnored = data.get('gradeTrustIgnored')
        self.__hasWarnings = data.get('hasWarnings')
        self.__isExceptional = data.get('isExceptional')
        self.__progress = data.get('progress')
        self.__duration = timedelta(milliseconds=data.get('duration'))
        self.__eta = timedelta(seconds=data.get('eta'))
        self.__delegation = data.get('delegation')
        if 'details' in data:
            self.__details = EndpointDetails(data['details'])
        else:
            self.__details = None
    @property
    def ipAddress(self):
        '''endpoint IP address, in IPv4 or IPv6 format.'''
        return self.__ipAddress
    @property
    def serverName(self):
        '''server name retrieved via reverse DNS'''
        return self.__serverName
    @property
    def statusMessage(self):
        '''assessment status message; this field will contain "Ready" if the
        endpoint assessment was successful.'''
        return self.__statusMessage
    @property
    def statusDetails(self):
        '''code of the operation currently in progress'''
        return self.__statusDetails
    @property
    def statusDetailsMessage(self):
        '''description of the operation currently in progress'''
        return self.__statusDetailsMessage
    @property
    def grade(self):
        '''possible values: A+, A-, A-F, T (no trust) and M (certificate name
        mismatch)'''
        return self.__grade
    @property
    def gradeTrustIgnored(self):
        '''grade (as above), if trust issues are ignored'''
        return self.__gradeTrustIgnored
    @property
    def hasWarnings(self):
        '''if this endpoint has warnings that might affect the score (e.g., get
        A- instead of A).'''
        return self.__hasWarnings
    @property
    def isExceptional(self):
        '''this flag will be raised when an exceptional configuration is
        encountered. The SSL Labs test will give such sites an A+.'''
        return self.__isExceptional
    @property
    def progress(self):
        '''assessment progress, which is a value from 0 to 100, and -1 if the
        assessment has not yet started'''
        return self.__progress
    @property
    def duration(self):
        '''assessment duration, as a timedelta'''
        return self.__duration
    @property
    def eta(self):
        '''estimated time, as a timedelta, until the completion of the
        assessment'''
        return self.__eta
    @property
    def delegation(self):
        '''indicates domain name delegation with and without the www prefix bit
        0 (1) - set for non-prefixed access bit 1 (2) - set for prefixed
        access'''
        return self.__delegation
    @property
    def details(self):
        '''this field contains an EndpointDetails object.'''
        return self.__details
