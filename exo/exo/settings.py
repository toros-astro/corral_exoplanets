#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-04-19T13:56:17.913405 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""Global configuration for exo

"""


# =============================================================================
# IMPORTS
# =============================================================================

import logging
import os


# =============================================================================
# CONFIGURATIONS
# =============================================================================

#: Path where the settings.py lives
PATH = os.path.abspath(os.path.dirname(__file__))

#: Run the steps and alerts with the debug number of processes
DEBUG_PROCESS = True

#: Sets the threshold for this logger to lvl. Logging messages which are less
#: severe than lvl will be ignored
LOG_LEVEL = logging.DEBUG

#: Template of string representation of every log of exo format
#: see: https://docs.python.org/2/library/logging.html#logrecord-attributes
LOG_FORMAT = (
        "[exo-%(name)s-%(levelname)s@%(asctime)-15s] %(message)s")


PIPELINE_SETUP = "exo.pipeline.Pipeline"


#: Database connection string formated ad the URL is an RFC-1738-style string.
#: See: http://docs.sqlalchemy.org/en/latest/core/engines.html
CONNECTION = "sqlite:///exo-dev.db"


# Loader class
LOADER = "exo.load.Loader"


# Pipeline processor steps
STEPS = [
    "exo.steps.HabitableZone"
]


# The alerts
ALERTS = ["exo.alerts.PlotAlert"]

# This values are autoimported when you open the shell
SHELL_LOCALS = {}


# SMTP server configuration
EMAIL = {
    "server": "",
    "tls": True,
    "user": "",
    "password": ""
}

MIGRATIONS_SETTINGS = os.path.join(PATH, "migrations", "alembic.ini")

PATH = os.path.abspath(os.path.dirname(__file__))
EXO_PATH = os.path.join(PATH, "data/exoplanets.csv")
