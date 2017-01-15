#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from ssllabs.object import Object

class StatusCodes(Object):
    '''Status codes, returned from :meth:`ssllabs.client.Client.statusCodes`'''
    def __init__(self, data):
        self.__statusDetails = data.get('statusDetails')

    @property
    def statusDetails(self):
        '''a :class:`dict` containing all status details codes and the
        corresponding English translations. Please note that, once in use, the
        codes will not change, whereas the translations may change at any
        time.'''
        return self.__statusDetails
