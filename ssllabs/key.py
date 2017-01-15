#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from ssllabs.object import Object

class Key(Object):
    '''Endpoint Key, accessed from
    :meth:`ssllabs.endpointdetails.EndpointDetails.key`'''
    def __init__(self, data):
        self.__size = data.get('size')
        self.__strength = data.get('strength')
        self.__alg = data.get('alg')
        self.__debianFlaw = data.get('debianFlaw')
        self.__q = data.get('q')

    @property
    def size(self):
        '''key size, e.g., 1024 or 2048 for RSA and DSA, or 256 bits for EC'''
        return self.__size
    @property
    def strength(self):
        '''key size expressed in RSA bits.'''
        return self.__strength
    @property
    def alg(self):
        '''key algorithm; possible values: RSA, DSA, and EC.'''
        return self.__alg
    @property
    def debianFlaw(self):
        '''true if we suspect that the key was generated using a weak random
        number generator (detected via a blacklist database)'''
        return self.__debianFlaw
    @property
    def q(self):
        '''0 if key is insecure, null otherwise'''
        return self.__q
