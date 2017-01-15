#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from ssllabs.object import Object

class DrownHost(Object):
    '''A DROWN host, accessed from
    :meth:`ssllabs.endpointdetails.EndpointDetails.drownHosts`'''
    def __init__(self, data):
        self.__ip = data.get('ip')
        self.__export = data.get('export')
        self.__port = data.get('port')
        self.__special = data.get('special')
        self.__sslv2 = data.get('sslv2')
        self.__status = data.get('status')

    @property
    def ip(self):
        '''Ip address of server that shares same RSA-Key/hostname in its
        certificate'''
        return self.__ip

    @property
    def export(self):
        '''true if export cipher suites detected'''
        return self.__export

    @property
    def port(self):
        '''port number of the server'''
        return self.__port

    @property
    def special(self):
        '''true if vulnerable OpenSSL version detected'''
        return self.__special

    @property
    def sslv2(self):
        '''true if SSL v2 is supported'''
        return self.__sslv2

    @property
    def status(self):
        '''drown host status:

        error
            error occurred in test
        unknown
            before the status is checked
        not_checked
            not checked if already vulnerable server found
        not_checked_same_host
            Not checked (same host)
        handshake_failure
            when SSL v2 not supported by server
        sslv2
            SSL v2 supported but not same rsa key
        key_match
            vulnerable (same key with SSL v2)
        hostname_match
            vulnerable (same hostname with SSL v2)
        '''
        return self.__status
