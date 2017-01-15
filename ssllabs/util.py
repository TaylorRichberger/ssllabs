#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

def objectornone(type, data, key):
    '''conditionally returns type(data[key]), or None.
    
    Checks data for key, returning a type object constructed with the value if
    it exists.

    :param type type: the type to be constructed from data[key]
    :param dict data: the data to use to construct the type object
    :param str key: the key to search for in data
    :returns: the type object, or None
    :rtype: the type contained in type, or NoneType
    '''
    if key in data:
        return type(data[key])
