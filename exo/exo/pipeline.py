#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-04-19T13:56:17.913405 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""Exo planets

"""

# =============================================================================
# IMPORTS
# =============================================================================

from corral.setup import PipelineSetup


# =============================================================================
# CONFIGURATION
# =============================================================================

class Pipeline(PipelineSetup):
    """This is an example pipeline using a custom version of the Exoplanets
    dataset (http://exoplanets.org/).

    """

    name = "Habitable Exo-Planets"
