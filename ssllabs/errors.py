#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

'''These are some general purpose errors, including errors generated for status
codes.  See `the API page for more information
<https://github.com/ssllabs/ssllabs-scan/blob/stable/ssllabs-api-docs.md#error-response-status-codes>`__.'''

class NoHostError(RuntimeError):
    '''An error indicating that no host had been set when
    :meth:`ssllabs.client.Client.host` was called.'''
    pass

class ResponseError(RuntimeError):
    '''The top-level response error.  This is never constructed directly'''
    pass

class ClientError(ResponseError):
    '''The mid-level response error indicating a 400-range error.  This is
    never constructed directy'''
    pass

class ServerError(ResponseError):
    '''The mid-level response error indicating a 500-range error.  This is
    never constructed directy'''
    pass

class InvocationError(ClientError):
    '''invocation error (e.g., invalid parameters)'''
    def __init__(self, reason):
        super(InvocationError, self).__init__('Invoked with invalid parameters. This is a library bug; please report it: {}'.format(reason))

class RequestRate(ClientError):
    '''client request rate too high or too many new assessments too fast'''
    def __init__(self, reason):
        super(RequestRate, self).__init__('Request rate is too high.  Please slow down: {}'.format(reason))

class InternalError(ServerError):
    '''internal error'''
    def __init__(self, reason):
        super(InternalError, self).__init__('Internal server error encountered.  Wait and try again: {}'.format(reason))

class ServiceNotAvailable(ServerError):
    '''the service is not available (e.g., down for maintenance)'''
    def __init__(self, reason):
        super(ServiceNotAvailable, self).__init__('Service not available.  May be down for maintenance.  Wait and try again: {}'.format(reason))

class ServiceOverloaded(ServerError):
    '''the service is overloaded'''
    def __init__(self, reason):
        super(ServiceOverloaded, self).__init__('Service overloaded.  Wait and try again: {}'.format(reason))

codes = {
    400: InvocationError,
    429: RequestRate,
    500: InternalError,
    503: ServiceNotAvailable,
    529: ServiceOverloaded,
    }
