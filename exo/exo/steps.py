#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-04-19T13:56:17.913405 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""exo steps

"""


# =============================================================================
# IMPORTS
# =============================================================================

import random

from corral import run

import numpy as np

from . import models


# =============================================================================
# CONSTANTS
# =============================================================================

STEFAN_BOLTZMANN = 5.670367e-8

SUN_LUMINOSITY = 3.828e26


# =============================================================================
# STEPS
# =============================================================================

class HabitableZone(run.Step):
    """Calculate some statistics of the star of a given planet
    and then determines if is in their habitable zone.

    """

    model = models.Planet
    conditions = [model.rstar != None, model.teff != None]

    def process(self, planet):
        # calculate the habitable zone of the host star
        luminosity = (
            STEFAN_BOLTZMANN * 4 * np.pi *
            (planet.rstar ** 2) * (planet.teff ** 4))
        lratio = luminosity / SUN_LUMINOSITY
        rin = np.sqrt(lratio / 1.1)
        rout = np.sqrt(lratio / 0.53)

        # verifiying if the planet is in habitable zone
        in_hz = planet.sep >= rin and planet.sep <= rout
        in_hz = random.choice((True, False))
        return models.HabitableZoneStats(
            planet=planet, in_habitable_zone=in_hz,
            luminosity=lratio, radio_inner=rin, radio_outer=rout)
