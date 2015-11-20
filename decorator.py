#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: decorator.py
Author: zlamberty
Created: 2015-11-20

Description:
    since python uses the word decorator, it is important to stress right away:
    though the purpose of the pythonic decorator and the decorator design
    pattern are not the same thing. The @ decorator in python are more similar
    to macros -- modify python objects/functions simply. The focus of the
    decorator dp is to extend an object's methods while preserving its
    interface and not subclassing. The same behavior could be implemented USING
    decorators, perhaps, or mix-in metaclasses, but they are not strictly the
    same thing (e.g. a python @ decorator modifes and returns the same class,
    so identity is maintained; the dp would give you a similar-looking but
    fundamentally different object)

    Nearest analogues of Python decorators in other languages are sometimes
    called annotations

Usage:
    <usage>

"""

import composite


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

CODES = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
}
ENDCODE = '\033[0m'


# ----------------------------- #
#   decorator classes           #
# ----------------------------- #

class ColorFileObj(composite.FileObject):
    """ a wrapper to the directory class that makes sure all directory lines and
        sublines are printed in a given color
    """
    def __init__(self, fileobj, color):
        self.fileobj = fileobj
        self.color = color
        self.startcode = CODES[self.color]

    # file operations
    def display(self, depth=0):
        return '{}{}{}'.format(
            self.startcode, self.fileobj.display(depth), ENDCODE
        )

    # hierarchy operations
    def add(self, f):
        self.fileobj.add(f)

    def remove(self, f):
        self.fileobj.remove(f)

    def get_child(self, i):
        self.fileobj.get_child(i)


def main():
    """ same as the main in composite.py, but now pr0n is red and user is
        blue. What? It's been a hard week!
    """
    # create a hierarchy
    print "\n{:*<80}".format("*** creating a hierarchy ")
    root = composite.Directory('/')
    etc = composite.Directory('etc')
    usr = ColorFileObj(composite.Directory('usr'), 'blue')
    pr0n = ColorFileObj(composite.Directory('pr0n'), 'red')

    root.add(etc)
    root.add(usr)
    usr.add(pr0n)

    fstab = composite.File('fstab.conf')
    fshoot = ColorFileObj(composite.File('fshoot.conf'), 'green')
    mlp = composite.File('mlp.mp9')

    etc.add(fstab)
    etc.add(fshoot)
    pr0n.add(mlp)

    # print
    print root.display()

    # remove a directory
    print "\n{:*<80}".format("*** quick, some one's coming! ")
    usr.remove(pr0n)

    # print
    print root.display()

    # remove a file
    print "\n{:*<80}".format("*** obama took ur gun ")
    etc.remove(fshoot)

    # print
    print root.display()



# ----------------------------- #
#   Command line                #
# ----------------------------- #

if __name__ == '__main__':
    main()
