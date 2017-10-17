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

import csv
import tempfile
import os
import shutil

import mock

from corral import qa
from corral.conf import settings

from . import models, steps, load, alerts



# =============================================================================
# LOADER
# =============================================================================

class LoadTest(qa.TestCase):

    subject = load.Loader

    def setup(self):
        with open(settings.EXO_PATH) as fp:
            reader = csv.DictReader(fp)
            self.total = len(list(reader))

    def validate(self):
        self.assertStreamCount(self.total, models.Planet)


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


class InHabitableZoneAlertTest(qa.TestCase):

    subject = alerts.InHabitableZoneAlert

    def setup(self):
        self.data_path = tempfile.mkdtemp()
        self.log_path = os.path.join(self.data_path, "in_habzone.log")
        self.plot_path = os.path.join(self.data_path, "in_habzone.png")
        self.alert_to = [
            alerts.ep.File(self.log_path),
            alerts.LogScatter(self.plot_path, xfield="per", yfield="mass",
                              title="Period Vs Mass - Habitable Zone",
                              marker="*")]
        self.patch("exo.alerts.InHabitableZoneAlert.alert_to", self.alert_to)


    def validate(self):
        self.assertTrue(os.path.exists(self.log_path))
        self.assertTrue(os.path.exists(self.plot_path))

    def teardown(self):
        # clean the temporary file so we do not leave trash behind us
        shutil.rmtree(self.data_path)
