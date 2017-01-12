#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

class Object(object):
    def __new__(typ, data):
        obj = object.__new__(typ)
        obj.__rawdata = data
        return obj

    @property
    def rawdata(self):
        '''The raw data as returned from the call and decoded, with no further
        processing done.
        
        This is provided because all objects should make the raw data available
        to users who may need or want to access it without forgoing the entire
        module'''
        return self.__rawdata
