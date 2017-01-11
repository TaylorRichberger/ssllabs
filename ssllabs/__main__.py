#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals
import six

import locale
import argparse

def gradecheck():
    locale.setlocale(locale.LC_ALL, '')
    parser = argparse.ArgumentParser(description='Do Something')
    parser.add_argument('-V', '--version', action='version', version='0.1')
    args = parser.parse_args()

if __name__ == '__main__':
    gradecheck()
