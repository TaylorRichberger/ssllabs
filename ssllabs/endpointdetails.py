#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta
import codecs

from ssllabs.cert import Cert
from ssllabs.object import Object

class EndpointDetails(Object):
    '''Detailed information about an endpoint'''

    def __init__(self, data):
        self.__hostStartTime = datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['hostStartTime'])
        self.__key = data.get('key')
        self.__cert = Cert(data.get('cert'))
        self.__chain = data.get('chain')
        self.__protocols = data.get('protocols')
        self.__suites = data.get('suites')
        self.__serverSignature = data.get('serverSignature')
        self.__prefixDelegation = data.get('prefixDelegation')
        self.__nonPrefixDelegation = data.get('nonPrefixDelegation')
        self.__vulnBeast = data.get('vulnBeast')
        self.__renegSupport = data.get('renegSupport')
        self.__sessionResumption = data.get('sessionResumption')
        self.__compressionMethods = data.get('compressionMethods')
        self.__supportsNpn = data.get('supportsNpn')
        self.__npnProtocols = data.get('npnProtocols', '').split(' ')
        self.__sessionTickets = data.get('sessionTickets')
        self.__ocspStapling = data.get('ocspStapling')
        self.__staplingRevocationStatus = data.get('staplingRevocationStatus')
        self.__staplingRevocationErrorMessage = data.get('staplingRevocationErrorMessage')
        self.__sniRequired = data.get('sniRequired')
        self.__httpStatusCode = data.get('httpStatusCode')
        self.__httpForwarding = data.get('httpForwarding')
        self.__supportsRc4 = data.get('supportsRc4')
        self.__rc4WithModern = data.get('rc4WithModern')
        self.__rc4Only = data.get('rc4Only')
        self.__forwardSecrecy = data.get('forwardSecrecy')
        self.__protocolIntolerance = data.get('protocolIntolerance')
        self.__miscIntolerance = data.get('miscIntolerance')
        self.__sims = data.get('sims')
        self.__heartbleed = data.get('heartbleed')
        self.__heartbeat = data.get('heartbeat')
        self.__openSslCcs = data.get('openSslCcs')
        self.__openSSLLuckyMinus20 = data.get('openSSLLuckyMinus20')
        self.__poodle = data.get('poodle')
        self.__poodleTls = data.get('poodleTls')
        self.__fallbackScsv = data.get('fallbackScsv')
        self.__freak = data.get('freak')
        self.__hasSct = data.get('hasSct')
        self.__dhPrimes = [codecs.decode(prime, 'hex_codec') for prime in data.get('dhPrimes', list())]
        self.__dhUsesKnownPrimes = data.get('dhUsesKnownPrimes')
        self.__dhYsReuse = data.get('dhYsReuse')
        self.__logjam = data.get('logjam')
        self.__chaCha20Preference = data.get('chaCha20Preference')
        self.__hstsPolicy = data.get('hstsPolicy')
        self.__hstsPreloads = data.get('hstsPreloads')
        self.__hpkpPolicy = data.get('hpkpPolicy')
        self.__hpkpRoPolicy = data.get('hpkpRoPolicy')
        self.__drownHosts = data.get('drownHosts')
        self.__drownErrors = data.get('drownErrors')
        self.__drownVulnerable = data.get('drownVulnerable')
    @property
    def hostStartTime(self):
        '''endpoint assessment starting time, in milliseconds since 1970. This
        field is useful when test results are retrieved in several HTTP
        invocations. Then, you should check that the hostStartTime value
        matches the startTime value of the host.'''
        return self.__hostStartTime
    @property
    def key(self):
        '''key information'''
        return self.__key
    @property
    def cert(self):
        '''certificate information as a :class:`ssllabs.cert.Cert`'''
        return self.__cert
    @property
    def chain(self):
        '''chain information'''
        return self.__chain
    @property
    def protocols(self):
        '''supported protocols'''
        return self.__protocols
    @property
    def suites(self):
        '''supported cipher suites'''
        return self.__suites
    @property
    def serverSignature(self):
        '''Contents of the HTTP Server response header when known. This field
        could be absent for one of two reasons: 1) the HTTP request failed
        (check httpStatusCode) or 2) there was no Server response header
        returned.'''
        return self.__serverSignature
    @property
    def prefixDelegation(self):
        '''true if this endpoint is reachable via a hostname with the www
        prefix'''
        return self.__prefixDelegation
    @property
    def nonPrefixDelegation(self):
        '''true if this endpoint is reachable via a hostname without the www
        prefix'''
        return self.__nonPrefixDelegation
    @property
    def vulnBeast(self):
        '''true if the endpoint is vulnerable to the BEAST attack'''
        return self.__vulnBeast
    @property
    def renegSupport(self):
        '''this is an integer value that describes the endpoint support for
        renegotiation: bit 0 (1) - set if insecure client-initiated
        renegotiation is supported bit 1 (2) - set if secure renegotiation is
        supported bit 2 (4) - set if secure client-initiated renegotiation is
        supported bit 3 (8) - set if the server requires secure renegotiation
        support'''
        return self.__renegSupport
    @property
    def sessionResumption(self):
        '''this is an integer value that describes endpoint support for session
        resumption. The possible values are: 0 - session resumption is not
        enabled and we're seeing empty session IDs 1 - endpoint returns session
        IDs, but sessions are not resumed 2 - session resumption is enabled'''
        return self.__sessionResumption
    @property
    def compressionMethods(self):
        '''integer value that describes supported compression methods bit 0 is
        set for DEFLATE'''
        return self.__compressionMethods
    @property
    def supportsNpn(self):
        '''true if the server supports NPN'''
        return self.__supportsNpn
    @property
    def npnProtocols(self):
        '''list of supported protocols'''
        return self.__npnProtocols
    @property
    def sessionTickets(self):
        '''indicates support for Session Tickets bit 0 (1) - set if session
        tickets are supported bit 1 (2) - set if the implementation is faulty
        [not implemented] bit 2 (4) - set if the server is intolerant to the
        extension'''
        return self.__sessionTickets
    @property
    def ocspStapling(self):
        '''true if OCSP stapling is deployed on the server'''
        return self.__ocspStapling
    @property
    def staplingRevocationStatus(self):
        '''same as :meth:`ssllabs.cert.Cert.revocationStatus`, but for the
        stapled OCSP response.'''
        return self.__staplingRevocationStatus
    @property
    def staplingRevocationErrorMessage(self):
        '''description of the problem with the stapled OCSP response, if
        any.'''
        return self.__staplingRevocationErrorMessage
    @property
    def sniRequired(self):
        '''if SNI support is required to access the web site.'''
        return self.__sniRequired
    @property
    def httpStatusCode(self):
        '''status code of the final HTTP response seen. When submitting HTTP
        requests, redirections are followed, but only if they lead to the same
        hostname. If this field is not available, that means the HTTP request
        failed.'''
        return self.__httpStatusCode
    @property
    def httpForwarding(self):
        '''available on a server that responded with a redirection to some
        other hostname.'''
        return self.__httpForwarding
    @property
    def supportsRc4(self):
        '''true if the server supports at least one RC4 suite.'''
        return self.__supportsRc4
    @property
    def rc4WithModern(self):
        '''true if RC4 is used with modern clients.'''
        return self.__rc4WithModern
    @property
    def rc4Only(self):
        '''true if only RC4 suites are supported.'''
        return self.__rc4Only
    @property
    def forwardSecrecy(self):
        '''indicates support for Forward Secrecy bit 0 (1) - set if at least
        one browser from our simulations negotiated a Forward Secrecy suite.
        bit 1 (2) - set based on Simulator results if FS is achieved with
        modern clients. For example, the server supports ECDHE suites, but not
        DHE.  bit 2 (4) - set if all simulated clients achieve FS. In other
        words, this requires an ECDHE + DHE combination to be supported.'''
        return self.__forwardSecrecy
    @property
    def protocolIntolerance(self):
        '''indicates protocol version intolerance issues: bit 0 (1) - TLS 1.0
        bit 1 (2) - TLS 1.1 bit 2 (4) - TLS 1.2 bit 3 (8) - TLS 1.3 bit 4 (16)
        - TLS 1.152 bit 5 (32) - TLS 2.152'''
        return self.__protocolIntolerance
    @property
    def miscIntolerance(self):
        '''indicates various other types of intolerance: bit 0 (1) - extension
        intolerance bit 1 (2) - long handshake intolerance bit 2 (4) - long
        handshake intolerance workaround success'''
        return self.__miscIntolerance
    @property
    def sims(self):
        '''instance of SimDetails.'''
        return self.__sims
    @property
    def heartbleed(self):
        '''true if the server is vulnerable to the Heartbleed attack.'''
        return self.__heartbleed
    @property
    def heartbeat(self):
        '''true if the server supports the Heartbeat extension.'''
        return self.__heartbeat
    @property
    def openSslCcs(self):
        '''results of the CVE-2014-0224 test: -1 - test failed 0 - unknown 1 -
        not vulnerable 2 - possibly vulnerable, but not exploitable 3 -
        vulnerable and exploitable'''
        return self.__openSslCcs
    @property
    def openSSLLuckyMinus20(self):
        '''results of the CVE-2016-2107 test: -1 - test failed 0 - unknown 1 -
        not vulnerable 2 - vulnerable and insecure'''
        return self.__openSSLLuckyMinus20
    @property
    def poodle(self):
        '''true if the endpoint is vulnerable to POODLE; false otherwise'''
        return self.__poodle
    @property
    def poodleTls(self):
        '''results of the POODLE TLS test: -3 - timeout -2 - TLS not supported
        -1 - test failed 0 - unknown 1 - not vulnerable 2 - vulnerable'''
        return self.__poodleTls
    @property
    def fallbackScsv(self):
        '''true if the server supports TLS_FALLBACK_SCSV, false if it doesn't.
        This field will not be available if the server's support for
        TLS_FALLBACK_SCSV can't be tested because it supports only one protocol
        version (e.g., only TLS 1.2).'''
        return self.__fallbackScsv
    @property
    def freak(self):
        '''true of the server is vulnerable to the FREAK attack, meaning it
        supports 512-bit key exchange.'''
        return self.__freak
    @property
    def hasSct(self):
        '''information about the availability of certificate transparency
        information (embedded SCTs): bit 0 (1) - SCT in certificate bit 1 (2) -
        SCT in the stapled OCSP response bit 2 (4) - SCT in the TLS extension
        (ServerHello)'''
        return self.__hasSct
    @property
    def dhPrimes(self):
        '''list of DH primes used by the server (as raw binary bytes objects).
        Not present if the server doesn't support the DH key exchange.'''
        return self.__dhPrimes
    @property
    def dhUsesKnownPrimes(self):
        '''whether the server uses known DH primes. Not present if the server
        doesn't support the DH key exchange. Possible values: 0 - no 1 - yes,
        but they're not weak 2 - yes and they're weak'''
        return self.__dhUsesKnownPrimes
    @property
    def dhYsReuse(self):
        '''true if the DH ephemeral server value is reused. Not present if the
        server doesn't support the DH key exchange.'''
        return self.__dhYsReuse
    @property
    def logjam(self):
        '''true if the server uses DH parameters weaker than 1024 bits.'''
        return self.__logjam
    @property
    def chaCha20Preference(self):
        '''true if the server takes into account client preferences when
        deciding if to use ChaCha20 suites.'''
        return self.__chaCha20Preference
    @property
    def hstsPolicy(self):
        '''server's HSTS policy. Experimental.'''
        return self.__hstsPolicy
    @property
    def hstsPreloads(self):
        '''information about preloaded HSTS policies.'''
        return self.__hstsPreloads
    @property
    def hpkpPolicy(self):
        '''server's HPKP policy. Experimental.'''
        return self.__hpkpPolicy
    @property
    def hpkpRoPolicy(self):
        '''server's HPKP RO (Report Only) policy. Experimental.'''
        return self.__hpkpRoPolicy
    @property
    def drownHosts(self):
        '''list of drown hosts. Experimental.'''
        return self.__drownHosts
    @property
    def drownErrors(self):
        '''true if error occurred in drown test.'''
        return self.__drownErrors
    @property
    def drownVulnerable(self):
        '''true if server vulnerable to drown attack.'''
        return self.__drownVulnerable
