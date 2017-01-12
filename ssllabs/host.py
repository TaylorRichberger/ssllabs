#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.endpoint import Endpoint
from ssllabs.object import Object

class Host(Object):
    def __init__(self, data):
        self.__host = data.get('host')
        self.__port = data.get('port')
        self.__protocol = data.get('protocol')
        self.__isPublic = data.get('isPublic')
        self.__status = data.get('status')
        self.__statusMessage = data.get('statusMessage')
        self.__startTime = datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['startTime'])
        self.__testTime = datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['testTime'])
        self.__engineVersion = data.get('engineVersion')
        self.__criteriaVersion = data.get('criteriaVersion')
        self.__cacheExpiryTime = data.get('cacheExpiryTime')
        self.__endpoints = [Endpoint(endpoint) for endpoint in data.get('endpoints', list())]
        self.__certHostnames = data.get('certHostnames', list())

    @property
    def host(self):
        '''assessment host, which can be a hostname or an IP address'''
        return self.__host
    @property
    def port(self):
        '''assessment port (e.g., 443)'''
        return self.__port
    @property
    def protocol(self):
        '''protocol (e.g., HTTP)'''
        return self.__protocol
    @property
    def isPublic(self):
        '''true if this assessment is publicly available (listed on the SSL
        Labs assessment boards)'''
        return self.__isPublic
    @property
    def status(self):
        '''assessment status; possible values: DNS, ERROR, IN_PROGRESS, and
        READY.'''
        return self.__status
    @property
    def statusMessage(self):
        '''status message in English. When status is ERROR, this field will
        contain an error message.'''
        return self.__statusMessage
    @property
    def startTime(self):
        '''assessment starting time, as a utc datetime object'''
        return self.__startTime
    @property
    def testTime(self):
        '''assessment completion time, as a utc datetime object'''
        return self.__testTime
    @property
    def engineVersion(self):
        '''assessment engine version (e.g., "1.0.120")'''
        return self.__engineVersion
    @property
    def criteriaVersion(self):
        '''grading criteria version (e.g., "2009")'''
        return self.__criteriaVersion
    @property
    def cacheExpiryTime(self):
        '''when will the assessment results expire from the cache (typically
        set only for assessment with errors; otherwise the results stay in the
        cache for as long as there's sufficient room)'''
        return self.__cacheExpiryTime
    @property
    def endpoints(self):
        '''list of Endpoint objects'''
        return self.__endpoints
    @property
    def certHostnames(self):
        '''the list of certificate hostnames collected from the
        certificates seen during assessment. The hostnames may not be
        valid. This field is available only if the server certificate
        doesn't match the requested hostname. In that case, this field
        saves you some time as you don't have to inspect the certificates
        yourself to find out what valid hostnames might be.'''
        return self.__certHostnames
