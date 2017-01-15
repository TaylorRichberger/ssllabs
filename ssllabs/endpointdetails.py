#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta
import codecs

from ssllabs.cert import Cert
from ssllabs.chain import Chain
from ssllabs.drownhost import DrownHost
from ssllabs.hpkppolicy import HpkpPolicy
from ssllabs.hstspolicy import HstsPolicy
from ssllabs.hstspreload import HstsPreload
from ssllabs.key import Key
from ssllabs.object import Object
from ssllabs.protocol import Protocol
from ssllabs.simdetails import SimDetails
from ssllabs.suites import Suites
from ssllabs.util import objectornone

class EndpointDetails(Object):
    '''Detailed information about an endpoint, accessed from
    :meth:`ssllabs.endpoint.Endpoint.details`'''

    def __init__(self, data):
        self.__hostStartTime = datetime.utcfromtimestamp(0) + timedelta(milliseconds=data['hostStartTime']) if 'hostStartTime' in data else None
        self.__key = objectornone(Key, data, 'key')
        self.__cert = objectornone(Cert, data, 'cert')
        self.__chain = objectornone(Chain, data, 'chain')
        self.__protocols = [Protocol(protocol) for protocol in data.get('protocols', list())]
        self.__suites = objectornone(Suites, data, 'suites')
        self.__serverSignature = data.get('serverSignature')
        self.__prefixDelegation = data.get('prefixDelegation')
        self.__nonPrefixDelegation = data.get('nonPrefixDelegation')
        self.__vulnBeast = data.get('vulnBeast')
        self.__renegSupport = objectornone(RenegSupport, data, 'renegSupport')
        self.__sessionResumption = data.get('sessionResumption')
        self.__compressionMethods = objectornone(CompressionMethods, data, 'compressionMethods')
        self.__supportsNpn = data.get('supportsNpn')
        self.__npnProtocols = data.get('npnProtocols', '').split(' ')
        self.__sessionTickets = objectornone(SessionTickets, data, 'sessionTickets')
        self.__ocspStapling = data.get('ocspStapling')
        self.__staplingRevocationStatus = data.get('staplingRevocationStatus')
        self.__staplingRevocationErrorMessage = data.get('staplingRevocationErrorMessage')
        self.__sniRequired = data.get('sniRequired')
        self.__httpStatusCode = data.get('httpStatusCode')
        self.__httpForwarding = data.get('httpForwarding')
        self.__supportsRc4 = data.get('supportsRc4')
        self.__rc4WithModern = data.get('rc4WithModern')
        self.__rc4Only = data.get('rc4Only')
        self.__forwardSecrecy = objectornone(ForwardSecrecy, data, 'forwardSecrecy')
        self.__protocolIntolerance = objectornone(ProtocolIntolerance, data, 'protocolIntolerance')
        self.__miscIntolerance = objectornone(MiscIntolerance, data, 'miscIntolerance')
        self.__sims = objectornone(SimDetails, data, 'sims')
        self.__heartbleed = data.get('heartbleed')
        self.__heartbeat = data.get('heartbeat')
        self.__openSslCcs = data.get('openSslCcs')
        self.__openSSLLuckyMinus20 = data.get('openSSLLuckyMinus20')
        self.__poodle = data.get('poodle')
        self.__poodleTls = data.get('poodleTls')
        self.__fallbackScsv = data.get('fallbackScsv')
        self.__freak = data.get('freak')
        self.__hasSct = objectornone(HasSct, data, 'hasSct')
        self.__dhPrimes = [codecs.decode(prime, 'hex_codec') for prime in data.get('dhPrimes', list())]
        self.__dhUsesKnownPrimes = data.get('dhUsesKnownPrimes')
        self.__dhYsReuse = data.get('dhYsReuse')
        self.__logjam = data.get('logjam')
        self.__chaCha20Preference = data.get('chaCha20Preference')
        self.__hstsPolicy = objectornone(HstsPolicy, data, 'hstsPolicy')
        self.__hstsPreloads = [HstsPreload(preload) for preload in data.get('hstsPreloads', list())]
        self.__hpkpPolicy = objectornone(HpkpPolicy, data, 'hpkpPolicy')
        self.__hpkpRoPolicy = objectornone(HpkpPolicy, data, 'hpkpRoPolicy')
        self.__drownHosts = [DrownHost(host) for host in data.get('drownHosts', list())]
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
        '''key information, as a :class:`ssllabs.key.Key`'''
        return self.__key
    @property
    def cert(self):
        '''certificate information as a :class:`ssllabs.cert.Cert`'''
        return self.__cert
    @property
    def chain(self):
        '''chain information, as a :class:`ssllabs.chain.Chain`'''
        return self.__chain
    @property
    def protocols(self):
        '''supported protocols, as a list of :class:`ssllabs.protocol.Protocol`'''
        return self.__protocols
    @property
    def suites(self):
        '''supported cipher suites, as a :class:`ssllabs.suites.Suites`'''
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
        '''this is :class:`RenegSupport` object that describes the endpoint
        support for renegotiation'''
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
        '''integer value that describes supported compression methods, as a
        :class:`CompressionMethods`'''
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
        '''indicates support for Session Tickets, as a :class:`SessionTickets`
        object'''
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
        '''indicates support for Forward Secrecy, as a :class:`ForwardSecrecy`
        object'''
        return self.__forwardSecrecy
    @property
    def protocolIntolerance(self):
        '''indicates protocol version intolerance issues as
        :class:`ProtocolIntolerance`'''
        return self.__protocolIntolerance
    @property
    def miscIntolerance(self):
        '''indicates various other types of intolerance as
        :class:`MiscIntolerance`'''
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
        information (embedded SCTs) as :class:`HasSct`'''
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
        '''server's HSTS policy as a :class:`ssllabs.hstspolicy.HstsPolicy`.
        Experimental.'''
        return self.__hstsPolicy
    @property
    def hstsPreloads(self):
        '''information about preloaded HSTS policies as a list of
        :class:`ssllabs.hstspreload.HstsPreload`'''
        return self.__hstsPreloads
    @property
    def hpkpPolicy(self):
        '''server's HPKP policy as a :class:`ssllabs.hpkppolicy.HpkpPolicy`.
        Experimental.'''
        return self.__hpkpPolicy
    @property
    def hpkpRoPolicy(self):
        '''server's HPKP RO (Report Only) policy as a
        :class:`ssllabs.hpkppolicy.HpkpPolicy`. Experimental.'''
        return self.__hpkpRoPolicy
    @property
    def drownHosts(self):
        '''list of drown hosts as :class:`ssllabs.drownhost.DrownHost`.
        Experimental.'''
        return self.__drownHosts
    @property
    def drownErrors(self):
        '''true if error occurred in drown test.'''
        return self.__drownErrors
    @property
    def drownVulnerable(self):
        '''true if server vulnerable to drown attack.'''
        return self.__drownVulnerable

class RenegSupport(object):
    '''support for renegotiation, from :meth:`EndpointDetails.renegSupport`'''
    def __init__(self, data):
        self.__clientinitiated = bool(1 & data)
        self.__secure = bool(2 & data)
        self.__secureclientinitiated = bool(4 & data)
        self.__serverrequiressecure = bool(8 & data)

    @property
    def clientinitiated(self):
        '''set if insecure client-initiated renegotiation is supported'''
        return self.__clientinitiated

    @property
    def secure(self):
        '''set if secure renegotiation is supported'''
        return self.__secure

    @property
    def secureclientinitiated(self):
        '''set if secure client-initiated renegotiation is supported'''
        return self.__secureclientinitiated

    @property
    def serverrequiressecure(self):
        '''set if the server requires secure renegotiation support'''
        return self.__serverrequiressecure

class CompressionMethods(object):
    '''supported compression methods, from :meth:`EndpointDetails.compressionMethods`'''
    def __init__(self, data):
        self.__deflate = bool(1 & data)

    @property
    def deflate(self):
        '''set for DEFLATE'''
        return self.__deflate

class SessionTickets(object):
    '''support for session tickets, from :meth:`EndpointDetails.sessionTickets`'''
    def __init__(self, data):
        self.__supported = bool(1 & data)
        self.__faulty = bool(2 & data)
        self.__intolerant = bool(4 & data)

    @property
    def supported(self):
        '''set if session tickets are supported'''
        return self.__supported

    @property
    def faulty(self):
        '''set if the implementation is faulty [not implemented]'''
        return self.__faulty

    @property
    def intolerant(self):
        '''set if the server is intolerant to the extension'''
        return self.__intolerant

class ForwardSecrecy(object):
    '''indicates support for Forward Secrecy, from :meth:`EndpointDetails.forwardSecrecy`'''
    def __init__(self, data):
        self.__negotiated = bool(1 & data)
        self.__modernacheived = bool(2 & data)
        self.__allacheived = bool(4 & data)

    @property
    def negotiated(self):
        '''set if at least one browser from our simulations negotiated a
        Forward Secrecy suite'''
        return self.__negotiated

    @property
    def modernacheived(self):
        '''set based on Simulator results if FS is achieved with modern
        clients. For example, the server supports ECDHE suites, but not DHE'''
        return self.__modernacheived

    @property
    def allacheived(self):
        '''set if all simulated clients achieve FS. In other words, this
        requires an ECDHE + DHE combination to be supported'''
        return self.__allacheived

class ProtocolIntolerance(object):
    '''indicates protocol version intolerance issues, from :meth:`EndpointDetails.protocolIntolerance`'''
    def __init__(self, data):
        self.__TLS_1_0 = bool(1 & data)
        self.__TLS_1_1 = bool(2 & data)
        self.__TLS_1_2 = bool(4 & data)
        self.__TLS_1_3 = bool(8 & data)
        self.__TLS_1_152 = bool(16 & data)
        self.__TLS_2_152 = bool(32 & data)

    @property
    def TLS_1_0(self):
        '''TLS 1.0'''
        return self.__TLS_1_0

    @property
    def TLS_1_1(self):
        '''TLS 1.1'''
        return self.__TLS_1_1

    @property
    def TLS_1_2(self):
        '''TLS 1.2'''
        return self.__TLS_1_2

    @property
    def TLS_1_3(self):
        '''TLS 1.3'''
        return self.__TLS_1_3

    @property
    def TLS_1_152(self):
        '''TLS 1.152'''
        return self.__TLS_1_152

    @property
    def TLS_2_152(self):
        '''TLS 2.152'''
        return self.__TLS_2_152

class MiscIntolerance(object):
    '''indicates various other types of intolerance, from :meth:`EndpointDetails.miscIntolerance`'''
    def __init__(self, data):
        self.__extensionintolerance = bool(1 & data)
        self.__longhandshakeintolerance = bool(2 & data)
        self.__longhandshakeworkaround = bool(4 & data)

    @property
    def extensionintolerance(self):
        '''extension intolerance'''
        return self.__extensionintolerance

    @property
    def longhandshakeintolerance(self):
        '''long handshake intolerance'''
        return self.__longhandshakeintolerance

    @property
    def longhandshakeworkaround(self):
        '''long handshake intolerance workaround success'''
        return self.__longhandshakeworkaround

class HasSct(object):
    '''information about the availability of certificate transparency
    information (embedded SCTs), from :meth:`EndpointDetails.hasSct`'''
    def __init__(self, data):
        self.__sctincertificate = bool(1 & data)
        self.__sctinstapledocsp = bool(2 & data)
        self.__sctintlsextension = bool(4 & data)

    @property
    def sctincertificate(self):
        '''SCT in certificate'''
        return self.__sctincertificate

    @property
    def sctinstapledocsp(self):
        '''SCT in the stapled OCSP response'''
        return self.__sctinstapledocsp

    @property
    def sctintlsextension(self):
        '''SCT in the TLS extension (ServerHello)'''
        return self.__sctintlsextension
