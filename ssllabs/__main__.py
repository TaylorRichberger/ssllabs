#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

import argparse
import locale
import six
import sys
from datetime import timedelta, datetime

from ssllabs.__init__ import __version__
from ssllabs.client import Client

__GRADE = (
    'A+', 'A', 'A-',
    'B+', 'B', 'B-',
    'C+', 'C', 'C-',
    'D+', 'D', 'D-',
    'E+', 'E', 'E-',
    'F+', 'F', 'F-',
    'T', 'M', 'EMPTY',
    )

def parsegrade(string):
    return __GRADE.index(string)

def gradecheck():
    locale.setlocale(locale.LC_ALL, '')
    parser = argparse.ArgumentParser(description='Do a grade check of a server.  For multi-endpoint setups, the worst grade of the cluster will be considered.  Returns 0 for a passing grade, and 1 for a failing grade.')
    parser.add_argument('-V', '--version', action='version', version=__version__)
    parser.add_argument('-g', '--grade', help='The minimum acceptable grade (default %(default)s)', type=parsegrade, default='A+')
    parser.add_argument('-T', '--ignoretrust', help='If this is set, Trust will be ignored and the trust-ignored grade will be used', action='store_true')
    parser.add_argument('-e', '--allowempty', help='If this is set, a test with 0 endpoints will be considered successful, rather than always unsuccessful', action='store_true')
    parser.add_argument('-x', '--expiretime', help='If this is set, set a time to warn for soon expiry (must be a number in days)', type=lambda s: timedelta(int(s)))
    group = parser.add_mutually_exclusive_group()
    #group.add_argument('-v', '--verbose', help='More output', action='store_true')
    group.add_argument('-q', '--quiet', help='Less output', action='store_true')
    parser.add_argument('host', help='The host to check')

    args = parser.parse_args()

    grade = None
    expiretime = None

    c = Client()
    data = c.analyze(args.host)

    getgrade = lambda endpoint: parsegrade(endpoint['gradeTrustIgnored'] if args.ignoretrust else endpoint['grade'])

    for endpoint in data['endpoints']:
        endpointgrade = getgrade(endpoint)
        endpointexpiretime = datetime.utcfromtimestamp(endpoint['details']['cert']['notAfter'] / 1000)
        if grade is None or grade < endpointgrade:
            grade = endpointgrade
        if expiretime is None or expiretime > endpointexpiretime:
            expiretime = endpointexpiretime

    timeleft = expiretime - datetime.utcnow()

    if grade is None:
        if args.allowempty:
            grade = parsegrade('A+')
        else:
            grade = parsegrade('EMPTY')

    if not args.quiet:
        print('Needed grade of {}, got grade of {}'.format(__GRADE[args.grade], __GRADE[grade]))

        if args.expiretime is not None:
            print('Needed expire time at least {.days} days away, {.days} days left, expiring on {:%c}'.format(args.expiretime, timeleft, expiretime))

    retval = 0

    if grade > args.grade:
        retval = 1

    if args.expiretime is not None and timeleft <= args.expiretime:
        retval = 1

    return retval

if __name__ == '__main__':
    sys.exit(gradecheck())
