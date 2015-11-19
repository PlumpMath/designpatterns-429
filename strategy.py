#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: strategy.py
Author: zlamberty
Created: 2015-11-18

Description:
    a simple strategy dp example using different scoring algorithms to
    evaluate a small fantasy football team's performance.

    Context: RosterWithScoring
    Strategy: ScoringStrategy
        OnePpr
        HalfPpr
        ZeroPpr
        Random

Usage:
    <usage>

"""

import os
import random

import ffl_player


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

FYAML = os.path.join('.', 'config', 'playerstats.yaml')
DEF_SCORE_FACTORS = {
    'completions': 0.1,
    'fumbles': -0.5,
    'incompletions': -0.1,
    'interceptions': -2.0,
    'p300': 0.5,
    'pass_tds': 6.0,
    'pass_yards': 0.04,
    'rec_tds': 6.0,
    'rec_yds': 0.1,
    'retd40': 0.5,
    'retd50': 0.5,
    'rey100': 0.5,
    'rush_yds': 0.1,
    'rushes': 0.1,
    'sacked': -0.5,
}


# ----------------------------- #
#   Strategy                    #
# ----------------------------- #

class ScoringStrategy(object):
    """ define scoring strat interface """
    def __init__(self, *args, **kwargs):
        raise NotImplementedError()

    def roster_score(self, roster):
        return sum(self.player_score(player) for player in roster.players)

    def player_score(self, player):
        return sum(
            self.scorefactors.get(stat, 0.0) * val
            for (stat, val) in player.stats.items()
        )


class OnePpr(ScoringStrategy):
    def __init__(self):
        self.scorefactors = DEF_SCORE_FACTORS
        self.scorefactors['receptions'] = 1.0


class HalfPpr(ScoringStrategy):
    def __init__(self):
        self.scorefactors = DEF_SCORE_FACTORS
        self.scorefactors['receptions'] = 0.5


class ZeroPpr(ScoringStrategy):
    def __init__(self):
        self.scorefactors = DEF_SCORE_FACTORS
        self.scorefactors['receptions'] = 0.0


class Random(ScoringStrategy):
    def __init__(self):
        self.scorefactors = DEF_SCORE_FACTORS
        self.scorefactors['receptions'] = random.random()


# ----------------------------- #
#   Context                     #
# ----------------------------- #

class RosterWithScoring(ffl_player.Roster):
    """ add a scoring algorithm option to the vanilla roster """
    def __init__(self, name, scoringMethod=OnePpr):
        super(RosterWithScoring, self).__init__(name)
        self.scoringMethod = scoringMethod

    def calculate_score(self):
        return self.scoringMethod.roster_score(roster=self)


# ----------------------------- #
#   Main routine                #
# ----------------------------- #

def main():
    """ docstring """
    r = RosterWithScoring('my_roster')
    ffl_player.update_from_yaml(r, FYAML)

    for strat in [OnePpr, HalfPpr, ZeroPpr, Random]:
        r.scoringMethod = strat()
        print 'strategy {:>7} score = {:.2f}'.format(
            type(r.scoringMethod).__name__, r.calculate_score()
        )


# ----------------------------- #
#   Command line                #
# ----------------------------- #

if __name__ == '__main__':
    main()
