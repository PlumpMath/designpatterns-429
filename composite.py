#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: composite.py
Author: zlamberty
Created: 2015-11-18

Description:
    composite design pattern

Usage:
    <usage>

"""

# ----------------------------- #
#   class definitions           #
# ----------------------------- #

class FileObject(object):
    """ the abstract "component" class; both directories and files will inherit
        from this
    """
    def __init__(self, name):
        raise NotImplementedError()

    # file operations
    def display(self, depth=0):
        print '{depth:}{name:}'.format(
            depth=' ' * depth,
            name = self.name
        )

    # hierarchy operations
    def add(self, f):
        raise ValueError("cannot add to file")

    def remove(self, f):
        raise ValueError("cannot remove from file")

    def get_child(self, i):
        raise ValueError("files have no children")


class Directory(FileObject):
    """ the directory is a named collection of files and directories """
    def __init__(self, name):
        self.name = name
        self.elements = []

    # file operations
    def display(self, depth=0):
        print '{depth:}{name:} (dir)'.format(
            depth=' ' * depth,
            name=self.name
        )

        for elem in self.elements:
            elem.display(depth=depth + 2)

    # hierarchy operations
    def add(self, f):
        self.elements.append(f)
        self.elements.sort()

    def remove(self, f):
        self.elements.remove(f)

    def get_child(self, i):
        return self.elements[i]


class File(FileObject):
    """ a file object """
    def __init__(self, name):
        self.name = name

    # all other functions defined in the base class


# ----------------------------- #
#   main routine                #
# ----------------------------- #

def main():
    """ create a directory structure from scratch and print it. Do some
        manipulations, print after each

    """
    # create a hierarchy
    print "\n{:*<80}".format("*** creating a hierarchy ")
    root = Directory('/')
    etc = Directory('etc')
    usr = Directory('usr')
    pr0n = Directory('pr0n')

    root.add(etc)
    root.add(usr)
    usr.add(pr0n)

    fstab = File('fstab.conf')
    fshoot = File('fshoot.conf')
    mlp = File('mlp.mp9')

    etc.add(fstab)
    etc.add(fshoot)
    pr0n.add(mlp)

    # print
    root.display()

    # remove a directory
    print "\n{:*<80}".format("*** quick, some one's coming! ")
    usr.remove(pr0n)

    # print
    root.display()

    # remove a file
    print "\n{:*<80}".format("*** obama took ur gun ")
    etc.remove(fshoot)

    # print
    root.display()


if __name__ == '__main__':
    main()
