#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.object import Object
from ssllabs.util import objectornone

class ChainCert(Object):
    '''Cert object that can be used to access the certificate of an
    :class:`ssllabs.chain.Chain`, accessed from
    :meth:`ssllabs.chain.Chain.certs`'''
    def __init__(self, data):
        self.__subject = data.get('subject')
        self.__label = data.get('label')
        self.__notBefore = (datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['notBefore'])) if 'notBefore' in data else None
        self.__notAfter = (datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['notAfter'])) if 'notAfter' in data else None
        self.__issuerSubject = data.get('issuerSubject')
        self.__issuerLabel = data.get('issuerLabel')
        self.__sigAlg = data.get('sigAlg')
        self.__issues = objectornone(Issues, data, 'issues')
        self.__keyAlg = data.get('keyAlg')
        self.__keySize = data.get('keySize')
        self.__keyStrength = data.get('keyStrength')
        self.__revocationStatus = data.get('revocationStatus')
        self.__crlRevocationStatus = data.get('crlRevocationStatus')
        self.__ocspRevocationStatus = data.get('ocspRevocationStatus')
        self.__raw = data.get('raw')

    @property
    def subject(self):
        '''certificate subject'''
        return self.__subject
    @property
    def label(self):
        '''certificate label (user-friendly name)'''
        return self.__label
    @property
    def notBefore(self):
        '''timestamp before which the certificate is not valid'''
        return self.__notBefore
    @property
    def notAfter(self):
        '''timestamp after which the certificate is not valid'''
        return self.__notAfter
    @property
    def issuerSubject(self):
        '''issuer subject'''
        return self.__issuerSubject
    @property
    def issuerLabel(self):
        '''issuer name'''
        return self.__issuerLabel
    @property
    def sigAlg(self):
        '''certificate signature algorithm'''
        return self.__sigAlg
    @property
    def issues(self):
        '''list of certificate issues as an :class:`Issues` object'''
        return self.__issues
    @property
    def keyAlg(self):
        '''certificate key algorithm'''
        return self.__keyAlg
    @property
    def keySize(self):
        '''certificate key size in bits'''
        return self.__keyAlg
    @property
    def keyStrength(self):
        '''certificate key strength, in equivalent RSA bits'''
        return self.__keyAlg
    @property
    def revocationStatus(self):
        '''a number that describes the revocation status of the certificate: 0
        - not checked 1 - certificate revoked 2 - certificate not revoked 3 -
        revocation check error 4 - no revocation information 5 - internal
        error'''
        return self.__revocationStatus
    @property
    def crlRevocationStatus(self):
        '''same as revocationStatus, but only for the CRL information (if
        any).'''
        return self.__crlRevocationStatus
    @property
    def ocspRevocationStatus(self):
        '''same as revocationStatus, but only for the OCSP information (if
        any).'''
        return self.__ocspRevocationStatus
    @property
    def raw(self):
        '''PEM-encoded certificate data'''
        return self.__raw

class Issues(object):
    '''Issues that may be present, from :meth:`ChainCert.issues`'''
    def __init__(self, data):
        self.__notyetvalid = bool(1 & data)
        self.__expired = bool(2 & data)
        self.__weakkey = bool(4 & data)
        self.__weaksignature = bool(8 & data)
        self.__blacklisted = bool(16 & data)

    @property
    def notyetvalid(self):
        '''certificate not yet valid'''
        return self.__notyetvalid

    @property
    def expired(self):
        '''certificate expired'''
        return self.__expired

    @property
    def weakkey(self):
        '''weak key'''
        return self.__weakkey

    @property
    def weaksignature(self):
        '''weak signature'''
        return self.__weaksignature

    @property
    def blacklisted(self):
        '''blacklisted'''
        return self.__blacklisted
