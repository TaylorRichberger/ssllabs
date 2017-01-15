#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.simclient import SimClient
from ssllabs.object import Object
from ssllabs.util import objectornone

class Simulation(Object):
    '''A single simulation, accessed from :meth:`ssllabs.simdetails.SimDetails.results`'''
    def __init__(self, data):
        self.__client = objectornone(SimClient, data, 'client')
        self.__errorCode = data.get('errorCode')
        self.__attempts = data.get('attempts')
        self.__protocolId = data.get('protocolId')
        self.__suiteId = data.get('suiteId')
        self.__kxInfo = data.get('kxInfo')

    @property
    def client(self):
        '''instance of :class:`ssllabs.simclient.SimClient`.'''
        return self.__client

    @property
    def errorCode(self):
        '''zero if handshake was successful, 1 if it was not.'''
        return self.__errorCode

    @property
    def attempts(self):
        '''always 1 with the current implementation.'''
        return self.__attempts

    @property
    def protocolId(self):
        '''Negotiated protocol ID.'''
        return self.__protocolId

    @property
    def suiteId(self):
        '''Negotiated suite ID.'''
        return self.__suiteId

    @property
    def kxInfo(self):
        '''key exchange info.'''
        return self.__kxInfo
