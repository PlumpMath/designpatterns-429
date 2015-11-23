#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: spaceship.py
Author: zlamberty
Created: 2015-11-23

Description:
    A module of spaceship objects. Blast off, suckas

Usage:
    <usage>

"""

import os


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

US_FLAG = os.path.join('config', 'usflag.asc')
UK_FLAG = os.path.join('config', 'ukflag.asc')


# ----------------------------- #
#   computer class              #
# ----------------------------- #

class Computer(object):
    """ abstract computer object """
    OFF, ON = 0, 1

    def __init__(self):
        raise NotImplementedError()

    def toggle_power(self):
        raise NotImplementedError()


class USComputer(Computer):
    """ AMERICA """
    def __init__(self):
        self.powerState = Computer.OFF

    def toggle_power(self):
        if self.powerState == Computer.OFF:
            print "\n *** starting up ... *** \n"
            print "\nYEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEHAW\n"
            with open(US_FLAG, 'r') as f:
                print f.read()
            print "\nWho wants to fight??\n"

            self.powerState = Computer.ON
        else:
            print "\n *** shutting down ... *** \n"
            print "\nMISSION ACCOMPLISHED!"
            self.powerState = Computer.OFF


class UKComputer(Computer):
    """ PRE-AMERICA """
    def __init__(self):
        self.powerState = Computer.OFF

    def toggle_power(self):
        if self.powerState == Computer.OFF:
            print "\n *** starting up ... *** \n"
            print "\npip pip guvnah up the apples an' all that \n"
            with open(UK_FLAG, 'r') as f:
                print f.read()
            print "\nWho wants some tea??\n"

            self.powerState = Computer.ON
        else:
            print "\n *** shutting down ... *** \n"
            print "\nGood show, chap!!"
            self.powerState = Computer.OFF


# ----------------------------- #
#   phasors class               #
# ----------------------------- #

class Phasors(object):
    """ abstract phasors object """
    STUN = 'stun'

    def __init__(self):
        raise NotImplementedError()

    def set_to(self, phasorMode=STUN):
        raise NotImplementedError()

    def fire(self):
        raise NotImplementedError()


class USPhasors(Phasors):
    """ AMERICA """
    AMERICA = "A*M*E*R*I*C*A"

    def __init__(self):
        print "beep boop beep boop\n"

    def set_to(self, phasorMode=Phasors.STUN):
        self.phasorMode = phasorMode
        print 'Phasors set to {}'.format(self.phasorMode)

    def fire(self):
        if self.phasorMode == Phasors.STUN:
            print "[EXECUTES STONE COLD STUNNER]"
            print "  ANDTHAT'S THE BOTTOM LINE"
            print "  BECAUSE STONE COLD"
            print "[POUNDS BEER]"
            print "  SAYS SO!"
        else:
            raise ValueError(
                'Phasor Mode {} not handled yet'.format(self.phasorMode)
            )


class UKPhasors(Phasors):
    """ PRE-AMERICA """
    UNITED_KINGDOM = "QUEENLOVERS"

    def __init__(self):
        print "beep boop beep boop"

    def set_to(self, phasorMode=Phasors.STUN):
        self.phasorMode = phasorMode
        print 'Phasors set to {}'.format(self.phasorMode)

    def fire(self):
        if self.phasorMode == Phasors.STUN:
            print "[stiff upper lift ENGAGED]"
            print "[passive aggressive politeness mode ACTIVATED]"
            print "  Why yes, your empire is pretty impressive, given how recently you started"
            print "[tosses empty gin bottle]"
            print "  Take that, you scoundrel"
        else:
            raise ValueError(
                'Phasor Mode {} not handled yet'.format(self.phasorMode)
            )
