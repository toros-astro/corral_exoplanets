#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-04-19T13:56:17.913405 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""exo database models

"""

# =============================================================================
# IMPORTS
# =============================================================================

from corral import db


# =============================================================================
# MODELS (Put your models below)
# =============================================================================

class Planet(db.Model):
    """Represent a single exoplanet.

    **Fields**

    - `name`: Name.
    - `mass`:
    - `sep`:
    - `dist`:
    - `mstar`:
    - `rstar`:
    - `teff`:
    - `fe`:

    """

    __tablename__ = 'Planet'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(40), nullable=False)
    per = db.Column(db.Float, nullable=True)
    mass = db.Column(db.Float, nullable=True)
    sep = db.Column(db.Float, nullable=True)
    dist = db.Column(db.Float, nullable=True)
    mstar = db.Column(db.Float, nullable=True)
    rstar = db.Column(db.Float, nullable=True)
    teff = db.Column(db.Float, nullable=True)
    fe = db.Column(db.Float, nullable=True)



class HabitableZoneStats(db.Model):
    """Resume of data about the capability of the planet
    to have life

    **Fields**

    - `planet`: Planet of the statistics
    - `luminosity`:
    - `radio_inner`:
    - `radio_outer`:
    - `in_habitable_zone`:

    """

    __tablename__ = "HabitableZoneStats"

    id = db.Column(db.Integer, primary_key=True)

    planet_id = db.Column(
        db.Integer, db.ForeignKey('Planet.id'), nullable=False)
    planet = db.relationship("Planet", backref=db.backref("hzones"))

    luminosity = db.Column(db.Float)
    radio_inner = db.Column(db.Float)
    radio_outer = db.Column(db.Float)

    in_habitable_zone = db.Column(db.Boolean)
