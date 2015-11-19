#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: ffl_player.py
Author: zlamberty
Created: 2015-11-18

Description:
    class for an ffl player

Usage:
    <usage>

"""

import yaml


# ----------------------------- #
#   Player class                #
# ----------------------------- #

class Stats(dict):
    pass


class Player(object):
    """ simple player object """
    def __init__(self, name, poslist):
        self.name = name
        self.poslist = poslist
        self.stats = Stats()

    def __repr__(self):
        return '<Player object {}>'.format(self.name)

    def __str__(self):
        return '{} ({})'.format(self.name, ', '.join(self.poslist))

    def update_stats(self, stats):
        """ given a dictionary of statistic: value pairs, add each as an
            attribute
        """
        self.stats.update(stats)


# ----------------------------- #
#   Roster class                #
# ----------------------------- #

class Roster(object):
    """ simple roster object """
    def __init__(self, name):
        self.name = name
        self.players = []

    def __repr__(self):
        return '<Roster object {}>'.format(self.name)

    def __str__(self):
        return '{}\n{}'.format(
            self.name,
            '\n'.join(str(p) for p in self.players)
        )

    def add(self, player):
        self.players.append(player)

    def remove(self, player):
        self.players.remove(player)


# ----------------------------- #
#   utility methods             #
# ----------------------------- #


def update_from_yaml(roster,  yamlFile):
    with open(yamlFile, 'rb') as f:
        for player in yaml.load(f):
            p = Player(name=player['name'], poslist=player['poslist'])
            p.update_stats(player['stats'])
            roster.add(p)


def roster_from_yaml(yamlFile, rosterName):
    r = Roster(rosterName)
    update_from_yaml(r, yamlFile)
    return r
