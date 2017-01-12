#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

class NoHostError(RuntimeError):
    pass

class ResponseError(RuntimeError):
    pass

class ClientError(ResponseError):
    pass

class ServerError(ResponseError):
    pass

class InvocationError(ClientError):
    def __init__(self, reason):
        super(InvocationError, self).__init__('Invoked with invalid parameters. This is a library bug; please report it: {}'.format(reason))

class RequestRate(ClientError):
    def __init__(self, reason):
        super(RequestRate, self).__init__('Request rate is too high.  Please slow down: {}'.format(reason))

class InternalError(ServerError):
    def __init__(self, reason):
        super(InternalError, self).__init__('Internal server error encountered.  Wait and try again: {}'.format(reason))

class ServiceNotAvailable(ServerError):
    def __init__(self, reason):
        super(ServiceNotAvailable, self).__init__('Service not available.  May be down for maintenance.  Wait and try again: {}'.format(reason))

class ServiceOverloaded(ServerError):
    def __init__(self, reason):
        super(ServiceOverloaded, self).__init__('Service overloaded.  Wait and try again: {}'.format(reason))

codes = {
    400: InvocationError,
    429: RequestRate,
    500: InternalError,
    503: ServiceNotAvailable,
    529: ServiceOverloaded,
    }
