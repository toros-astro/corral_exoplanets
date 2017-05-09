#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created at 2017-04-19T13:56:17.913405 by corral 0.2.6


# =============================================================================
# DOCS
# =============================================================================

"""exo alerts

"""


# =============================================================================
# IMPORTS
# =============================================================================

from corral import run
from corral.run import endpoints as ep

import numpy as np

from matplotlib import pyplot as plt

from exo import models

# =============================================================================
# ALERTS
# =============================================================================


class LogScatter(ep.EndPoint):

    def __init__(self, path, xfield, yfield, title, **kwargs):
        self.path = path
        self.xfield = xfield
        self.yfield = yfield
        self.title = title
        self.kwargs = kwargs
        self._x, self._y = [], []

    def process(self, hz):
        planet = hz.planet
        x, y = getattr(planet, self.xfield), getattr(planet, self.yfield)
        if x and y:
            self._x.append(x)
            self._y.append(y)

    def teardown(self, *args):
        plt.scatter(np.log(self._x), np.log(self._y), **self.kwargs)
        plt.title(self.title)
        plt.legend(loc="best")
        plt.savefig(self.path)
        super(LogScatter, self).teardown(*args)


class InHabitableZoneAlert(run.Alert):
    """Store a list of planets in habitable zone in a log file
    and also generate a period vs mass plot of this planets

    """

    model = models.HabitableZoneStats
    conditions = [model.in_habitable_zone == True]  # noqa
    alert_to = [
        ep.File("in_habzone.log"),
        LogScatter("in_habzone.png", xfield="per", yfield="mass",
                   title="Period Vs Mass - Habitable Zone", marker="*")]

    def render_alert(self, now, ep, hz):
        planet = hz.planet
        data = []
        for fn in planet.__table__.c:
            data.append([fn.name, getattr(planet, fn.name)])
        fields = ", ".join("{}={}".format(k, v) for k, v in data)
        return "[{}] {}\n".format(now.isoformat(), fields)
