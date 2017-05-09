#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-04-19T13:56:17.913405 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""exo tests

"""


# =============================================================================
# IMPORTS
# =============================================================================

from corral import qa

from . import models, steps


# =============================================================================
# LOADER
# =============================================================================

class HabitableZoneTest(qa.TestCase):

    subject = steps.HabitableZone

    def setup(self):
        planet = models.Planet(name="foo", rstar=1, teff=1)
        self.save(planet)

    def validate(self):
        planet = self.session.query(models.Planet).first()
        hzone = planet.hzones[0]
        self.assertAlmostEquals(hzone.luminosity, 8.962237975715271e-10)
        self.assertLess(hzone.radio_inner, hzone.radio_outer)
        self.assertFalse(hzone.in_habitable_zone)
        self.assertStreamCount(1, models.HabitableZoneStats)


class HabitableZoneNoRstarNoTeffTest(qa.TestCase):

    subject = steps.HabitableZone

    def setup(self):
        planet = models.Planet(name="foo")
        self.save(planet)

    def validate(self):
        self.assertStreamCount(0, models.HabitableZoneStats)
