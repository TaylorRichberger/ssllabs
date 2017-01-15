#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.chaincert import ChainCert
from ssllabs.object import Object
from ssllabs.util import objectornone

class Chain(Object):
    '''object that can be used to access the chain of an endpoint, accessed from :meth:`ssllabs.endpointdetails.EndpointDetails.chain`'''
    def __init__(self, data):
        self.__certs = [ChainCert(cert) for cert in data.get('certs', list())]
        self.__issues = objectornone(Issues, data, 'issues')
    @property
    def certs(self):
        '''a list of :class:`ssllabs.chaincert.ChainCert` objects, representing
        the chain certificates in the order in which they were retrieved from
        the server'''
        return self.__certs
    @property
    def issues(self):
        '''list of chain issues as an :class:`Issues` object'''
        return self.__issues

class Issues(object):
    '''Issues that may be present, from :meth:`Chain.issues`'''
    def __init__(self, data):
        self.__addedexternal = bool(1 & data)
        self.__incompletechain = bool(2 & data)
        self.__unrelated = bool(4 & data)
        self.__wrongorder = bool(8 & data)
        self.__selfsignedroot = bool(16 & data)
        self.__couldnotvalidate = bool(32 & data)

    @property
    def addedexternal(self):
        '''if we added external certificates'''
        return self.__addedexternal

    @property
    def incompletechain(self):
        '''incomplete chain (set only when we were able to build a chain by
        adding missing intermediate certificates from external sources)'''
        return self.__incompletechain

    @property
    def unrelated(self):
        '''chain contains unrelated or duplicate certificates (i.e.,
        certificates that are not part of the same chain)'''
        return self.__unrelated

    @property
    def wrongorder(self):
        '''the certificates form a chain (trusted or not), but the order is
        incorrect'''
        return self.__wrongorder

    @property
    def selfsignedroot(self):
        '''contains a self-signed root certificate (not set for self-signed
        leafs)'''
        return self.__selfsignedroot

    @property
    def couldnotvalidate(self):
        '''the certificates form a chain (if we added external certificates,
        :meth`addedexternal` will be set), but we could not validate it. If the
        leaf was trusted, that means that we built a different chain we
        trusted.'''
        return self.__couldnotvalidate

