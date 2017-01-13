#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

import argparse
import locale
import six
from time import sleep
import sys
from datetime import timedelta, datetime

from tqdm import tqdm

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

def average(numbers):
    return int(float(sum(numbers)) / max(len(numbers), 1))

def gradecheck():
    locale.setlocale(locale.LC_ALL, '')
    parser = argparse.ArgumentParser(description='Do a grade check of a server.  For multi-endpoint setups, the worst grade of the cluster will be considered.  Exits 0 for a passing grade, and 1 for a failing grade.  By using this tool, you are bound by the SSL Labs terms of use: https://www.ssllabs.com/about/terms.html.  This program sends data through the SSL Labs remote servers.')
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

    if not args.quiet:
        messagelist = '\n'.join(c.info().messages)
        if messagelist:
            print(messagelist)
            print()

    progress = None
    endpoints = list()

    for data in c.analyze(args.host):
        if data.status == 'DNS':
            sleep(1)
        else:
            if not args.quiet:
                if progress is None:
                    progress = [0, tqdm(desc="scanning", total=100, unit='%')]
                    endpoints = [[0, tqdm(postfix={'ip': endpoint.ipAddress, 'name': endpoint.serverName}, total=100, unit='%')] for endpoint in data.endpoints]

                for i in range(len(data.endpoints)):
                    endpoint = data.endpoints[i]
                    if endpoint.progress > 0:
                        diff = endpoint.progress - endpoints[i][0]
                        endpoints[i][0] = endpoint.progress
                        endpoints[i][1].update(diff)
                        endpoints[i][1].set_description(endpoint.statusDetailsMessage)
                newaverage = average([endpoint[0] for endpoint in endpoints])
                diff = newaverage - progress[0]
                progress[1].update(diff)
                progress[0] = newaverage
            sleep(3)

    if progress is not None:
        progress[1].close()
    for endpoint in endpoints:
        endpoint[1].close()

    data = c.host

    getgrade = lambda endpoint: parsegrade(endpoint.gradeTrustIgnored if args.ignoretrust else endpoint.grade)

    for endpoint in data.endpoints:
        if endpoint.grade is not None:
            endpointgrade = getgrade(endpoint)
            endpointexpiretime = endpoint.details.cert.notAfter
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

    if grade > args.grade:
        return 1

    if args.expiretime is not None and timeleft <= args.expiretime:
        return 1

    return 0

if __name__ == '__main__':
    sys.exit(gradecheck())
