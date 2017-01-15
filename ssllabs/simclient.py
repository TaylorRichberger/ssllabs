#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.object import Object

class SimClient(Object):
    '''A single simulation client, accessed from :meth:`ssllabs.simulation.Simulation.client`'''
    def __init__(self, data):
        self.__id = data.get('id')
        self.__name = data.get('name')
        self.__platform = data.get('platform')
        self.__version = data.get('version')
        self.__isReference = data.get('isReference')
    @property
    def id(self):
        '''unique client ID (integer)'''
        return self.__id

    @property
    def name(self):
        '''The client name'''
        return self.__name

    @property
    def platform(self):
        '''The client platform'''
        return self.__platform

    @property
    def version(self):
        '''The client version'''
        return self.__version

    @property
    def isReference(self):
        '''true if the browser is considered representative of modern browsers,
        false otherwise. This flag does not correlate to client's capabilities,
        but is used by SSL Labs to determine if a particular configuration is
        effective. For example, to track Forward Secrecy support, we mark
        several representative browsers as "modern" and then test to see if
        they succeed in negotiating a FS suite. Just as an illustration, modern
        browsers are currently Chrome, Firefox (not ESR versions), IE/Win7, and
        Safari.'''
        return self.__isReference
