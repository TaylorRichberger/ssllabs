#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from __future__ import division, absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from ssllabs.simulation import Simulation
from ssllabs.object import Object

class SimDetails(Object):
    '''Simulation collection, accessed from
    :meth:`ssllabs.endpointdetails.EndpointDetails.sims`'''
    def __init__(self, data):
        self.__results = [Simulation(simulation) for simulation in data.get('results', list())]
    @property
    def results(self):
        '''a list of :class:`ssllabs.simulation.Simulation` objects'''
        return self.__results
