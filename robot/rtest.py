#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:

    def act(self, game):
        poz = self.location
        poz2 = (poz[0] + 2, poz[1])
        print(poz2)
        dystans = rg.wdist(poz, poz2)
        print(dystans)

        dystansCP = rg.wdist(self.location, rg.CENTER_POINT)
        print(dystansCP)

        if dystansCP > 7:
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]

        # idź do środka planszy, ruch domyślny
        return ['move', rg.toward(self.location, rg.CENTER_POINT)]
