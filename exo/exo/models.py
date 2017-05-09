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
    - `per` : Period [days]
    - `mass`: Planet mass [solar masses]
    - `sep`: Star-planet Separation [AU]
    - `dist`: Distance to the star [pc]
    - `mstar`: Stellar mass [solar masses]
    - `rstar`: Stellar radius [solar radii]
    - `teff`: Effective temperature [K]
    - `fe`: Metallicity

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
    - `luminosity`: Stellar luminosity [solar luminosity]
    - `radio_inner`: Inner boundary of habitable zone [AU]
    - `radio_outer`: Outer boundary of habitable zone [AU]
    - `in_habitable_zone`: [boolean]

    """

    __tablename__ = "HabitableZoneStats"

    id = db.Column(db.Integer, primary_key=True)

    planet_id = db.Column(
        db.Integer, db.ForeignKey('Planet.id'), unique=True, nullable=False)
    planet = db.relationship("Planet", backref=db.backref("hzones"))

    luminosity = db.Column(db.Float)
    radio_inner = db.Column(db.Float)
    radio_outer = db.Column(db.Float)

    in_habitable_zone = db.Column(db.Boolean)
