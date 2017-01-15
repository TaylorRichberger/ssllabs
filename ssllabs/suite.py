#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.object import Object

class Suite(Object):
    '''Single cipher suite, accessed from :meth:`ssllabs.suites.Suites.list`'''
    def __init__(self, data):
        self.__id = data.get('id')
        self.__name = data.get('name')
        self.__cipherStrength = data.get('cipherStrength')
        self.__dhStrength = data.get('dhStrength')
        self.__dhP = data.get('dhP')
        self.__dhG = data.get('dhG')
        self.__dhYs = data.get('dhYs')
        self.__ecdhBits = data.get('ecdhBits')
        self.__ecdhStrength = data.get('ecdhStrength')
        self.__q = data.get('q')

        @property
        def id(self):
            '''suite RFC ID (e.g., 5)'''
            return self.__id

        @property
        def name(self):
            '''suite name (e.g., TLS_RSA_WITH_RC4_128_SHA)'''
            return self.__name

        @property
        def cipherStrength(self):
            '''suite strength (e.g., 128)'''
            return self.__cipherStrength

        @property
        def dhStrength(self):
            '''strength of DH params (e.g., 1024)'''
            return self.__dhStrength

        @property
        def dhP(self):
            '''DH params, p component'''
            return self.__dhP

        @property
        def dhG(self):
            '''DH params, g component'''
            return self.__dhG

        @property
        def dhYs(self):
            '''DH params, Ys component'''
            return self.__dhYs

        @property
        def ecdhBits(self):
            '''ECDH bits'''
            return self.__ecdhBits

        @property
        def ecdhStrength(self):
            '''ECDH RSA-equivalent strength'''
            return self.__ecdhStrength

        @property
        def q(self):
            '''0 if the suite is insecure, null otherwise'''
            return self.__q
