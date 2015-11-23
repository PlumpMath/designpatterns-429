#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: abstract_factory.py
Author: zlamberty
Created: 2015-11-23

Description:
    Abstract Factory example classes. These classes implement a factory for
    building spaceship components with different locale settings (US, UK)

Usage:
    <usage>

"""

import argparse
import time

import spaceship


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #


# ----------------------------- #
#   spaceship factory           #
# ----------------------------- #

class SpaceshipLocaleFactory(object):
    def __init__(self):
        raise NotImplementedError()

    def CreateComputer(self):
        raise NotImplementedError()

    def CreatePhasors(self):
        raise NotImplementedError()


class USSpaceshipFactory(SpaceshipLocaleFactory):
    def __init__(self):
        print "abfact: Init-ing {}".format(type(self).__name__)

    def CreateComputer(self):
        return spaceship.USComputer()

    def CreatePhasors(self):
        return spaceship.USPhasors()


class UKSpaceshipFactory(SpaceshipLocaleFactory):
    def __init__(self):
        print "abfact: Init-ing {}".format(type(self).__name__)

    def CreateComputer(self):
        return spaceship.UKComputer()

    def CreatePhasors(self):
        return spaceship.UKPhasors()


# ----------------------------- #
#   Main routine                #
# ----------------------------- #

def main(spaceshipFactory):
    """ blast off and blast em away """
    # create spaceship product objects with spaceship factory
    print "abfact: Building spaceship\n"
    comp = spaceshipFactory.CreateComputer()
    phas = spaceshipFactory.CreatePhasors()

    # turn on spaceship computer
    print "abfact: Turning on Computer"
    comp.toggle_power()

    # go to space
    for s in range(3, 0, -1):
        print "{}...".format(s)
        time.sleep(1)
    print "BLASTOFF\n"

    # phasors engaged
    print "abfact: Oh FUCK! An ALIEN!\n"
    phas.set_to(spaceship.Phasors.STUN)
    phas.fire()
    print "abfact: shew! That was close\n"

    # comping home
    print "abfact: We're home!"
    comp.toggle_power()


# ----------------------------- #
#   Command line                #
# ----------------------------- #

def parse_args():
    """ Take a log file from the commmand line """
    parser = argparse.ArgumentParser()
    locale = "The country locale of the spaceship and its users"
    parser.add_argument(
        "-l", "--locale", help=locale, choices=('US', 'UK'), required=True
    )

    return parser.parse_args()


if __name__ == '__main__':

    args = parse_args()

    if args.locale == 'US':
        spaceshipFactory = USSpaceshipFactory()
    elif args.locale == 'UK':
        spaceshipFactory = UKSpaceshipFactory()
    else:
        raise ValueError("Keeping it Colonial for the time being")

    main(spaceshipFactory)
