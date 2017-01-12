#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import timedelta
import six

from ssllabs.object import Object

class Info(Object):
    def __init__(self, data):
        self.__version = data.get('version')
        self.__criteriaVersion = data.get('criteriaVersion')
        self.__maxAssessments = data.get('maxAssessments')
        self.__currentAssessments = data.get('currentAssessments')
        self.__newAssessmentCoolOff = timedelta(milliseconds=data['newAssessmentCoolOff'])
        self.__messages = data.get('messages', list())
    @property
    def version(self):
        '''SSL Labs software version as a string (e.g., "1.11.14")'''
        return self.__version
    @property
    def criteriaVersion(self):
        '''rating criteria version as a string (e.g., "2009f")'''
        return self.__criteriaVersion
    @property
    def maxAssessments(self):
        '''the maximum number of concurrent assessments the client is allowed
        to initiate.'''
        return self.__maxAssessments
    @property
    def currentAssessments(self):
        '''the number of ongoing assessments submitted by this client.'''
        return self.__currentAssessments
    @property
    def newAssessmentCoolOff(self):
        '''the cool-off period after each new assessment, as a timedelta;
        you're not allowed to submit a new assessment before the cool-off
        expires, otherwise you'll get a 429.'''
        return self.__newAssessmentCoolOff
    @property
    def messages(self):
        '''a list of messages (strings). Messages can be public (sent to
        everyone) and private (sent only to the invoking client). Private
        messages are prefixed with "[Private]".'''
        return self.__messages
