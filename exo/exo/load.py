#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-04-19T13:56:17.913405 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""exo main loader

"""


# =============================================================================
# IMPORTS
# =============================================================================

import csv

from corral import run
from corral.conf import settings

from exo import models

# =============================================================================
# LOADER
# =============================================================================


class Loader(run.Loader):
    """Extract data from the `exoplanets.csv` and feed the stream
    of the pipeline.

    """

    def setup(self):
        # we open the file and assign it to an instance variable
        self.fp = open(settings.EXO_PATH)

    def float_or_none(self, value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    def generate(self):
        # now we make use of "self.fp" for the reader
        for row in csv.DictReader(self.fp):
            di = {
                'name': row['NAME'],
                'per': self.float_or_none(row['PER']),
                'mass': self.float_or_none(row['MASS']),
                'sep': self.float_or_none(row['SEP']),
                'dist': self.float_or_none(row['DIST']),
                'mstar': self.float_or_none(row['MSTAR']),
                'rstar': self.float_or_none(row['RSTAR']),
                'teff': self.float_or_none(row['TEFF']),
                'fe': self.float_or_none(row['FE'])}
            yield models.Planet(**di)

    def teardown(self, *args):
        # checking that the file is really open
        if self.fp and not self.fp.closed:
            self.fp.close()
