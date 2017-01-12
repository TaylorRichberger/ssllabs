#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.object import Object

class Cert(Object):
    '''Cert object that can be used to access the certificate of an endpoint'''
    def __init__(self, data):
        self.__subject = data.get('subject')
        self.__commonNames = data.get('commonNames')
        self.__altNames = data.get('altNames')
        self.__notBefore = datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['notBefore'])
        self.__notAfter = datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['notAfter'])
        self.__issuerSubject = data.get('issuerSubject')
        self.__sigAlg = data.get('sigAlg')
        self.__issuerLabel = data.get('issuerLabel')
        self.__revocationInfo = RevocationInfo(data['revocationInfo']) if 'revocationInfo' in data else None
        self.__crlURIs = data.get('crlURIs')
        self.__ocspURIs = data.get('ocspURIs')
        self.__revocationStatus = data.get('revocationStatus')
        self.__crlRevocationStatus = data.get('crlRevocationStatus')
        self.__ocspRevocationStatus = data.get('ocspRevocationStatus')
        self.__sgc = SGC(data['sgc']) if 'sgc' in data else None
        self.__validationType = data.get('validationType')
        self.__issues = Issues(data['issues']) if 'issues' in data else None
        self.__sct = data.get('sct')
        self.__mustStaple = data.get('mustStaple')
    @property
    def subject(self):
        '''certificate subject'''
        return self.__subject
    @property
    def commonNames(self):
        '''common names extracted from the subject'''
        return self.__commonNames
    @property
    def altNames(self):
        '''alternative names'''
        return self.__altNames
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
    def sigAlg(self):
        '''certificate signature algorithm'''
        return self.__sigAlg
    @property
    def issuerLabel(self):
        '''issuer name'''
        return self.__issuerLabel
    @property
    def revocationInfo(self):
        ''':class:`RevocationInfo` object representing revocation information
        present in the certificate'''
        return self.__revocationInfo
    @property
    def crlURIs(self):
        '''CRL URIs extracted from the certificate'''
        return self.__crlURIs
    @property
    def ocspURIs(self):
        '''OCSP URIs extracted from the certificate'''
        return self.__ocspURIs
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
    def sgc(self):
        '''Server Gated Cryptography support as an :class:`SGC` object'''
        return self.__sgc
    @property
    def validationType(self):
        '''E for Extended Validation certificates; may be null if unable to
        determine'''
        return self.__validationType
    @property
    def issues(self):
        '''list of certificate issues as an :class:`Issues` object'''
        return self.__issues
    @property
    def sct(self):
        '''true if the certificate contains an embedded SCT; false
        otherwise.'''
        return self.__sct
    @property
    def mustStaple(self):
        '''a number that describes the must staple feature extension status: 0
        - not supported 1 - Supported, but OCSP response is not stapled 2 -
        Supported, OCSP response is stapled'''
        return self.__mustStaple

class RevocationInfo(object):
    '''revocation information present in the certificate'''
    def __init__(self, data):
        self.__crl = bool(1 & data)
        self.__ocsp = bool(2 & data)
    @property
    def crl(self):
        '''CRL information available'''
        return self.__crl
    @property
    def ocsp(self):
        '''OCSP information available'''
        return self.__ocsp

class SGC(object):
    '''Server Gated Cryptography support'''
    def __init__(self, data):
        self.__netscape = bool(1 & data)
        self.__microsoft = bool(2 & data)
    @property
    def netscape(self):
        '''Netscape SGC'''
        return self.__netscape
    @property
    def microsoft(self):
        '''Microsoft SGC'''
        return self.__microsoft

class Issues(object):
    '''Issues that may be present'''
    def __init__(self, data):
        self.__nochainoftrust = bool(1 & data)
        self.__notbefore = bool(2 & data)
        self.__notafter = bool(4 & data)
        self.__hostnamemismatch = bool(8 & data)
        self.__revoked = bool(16 & data)
        self.__badcommonname = bool(32 & data)
        self.__selfsigned = bool(64 & data)
        self.__blacklisted = bool(128 & data)
        self.__insecuresignature = bool(256 & data)

    @property
    def nochainoftrust(self):
        '''No Chain of Trust'''
        return self.__nochainoftrust

    @property
    def notbefore(self):
        '''Violates Not Before constraint'''
        return self.__notbefore

    @property
    def notafter(self):
        '''Violates Not After constraint'''
        return self.__notafter

    @property
    def hostnamemismatch(self):
        '''Hostnames mismatched'''
        return self.__hostnamemismatch

    @property
    def revoked(self):
        '''Certificate revoked'''
        return self.__revoked

    @property
    def badcommonname(self):
        '''Bad Common Name'''
        return self.__badcommonname

    @property
    def selfsigned(self):
        '''Self-signed certificate'''
        return self.__selfsigned

    @property
    def blacklisted(self):
        '''Certificate blacklisted'''
        return self.__blacklisted

    @property
    def insecuresignature(self):
        '''Insecure Signature'''
        return self.__insecuresignature
