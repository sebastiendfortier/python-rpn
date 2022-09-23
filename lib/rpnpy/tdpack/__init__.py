#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Stephane Chamberland <stephane.chamberland@ec.gc.ca>
# Copyright: LGPL 2.1

"""
 Module tdpack is a ctypes import of tdpack's library (libtdpack.so)
 
 The libtdpack.so library is provided with the VGrid Descriptor package
 developed at CMC/RPN
 
 The tdpack python module includes
 - python wrapper to main libtdpack's functions
 - helper functions
 - prototypes for many libtdpack's functions
 - pre-defined constants
 - along with comprenhensive inline documentation

 See also:
    rpnpy.tdpack.proto
    rpnpy.tdpack.const
    rpnpy.tdpack.base

"""

from rpnpy.version import *

__SUBMODULES__ = ['proto', 'const', 'func', 'base']
__all__ = ['loadTDPACKlib', 'libtdpack', 'TDPACK_VERSION', 'TDPACK_LIBPATH',
           'TDPACKError'] + __SUBMODULES__

## TDPACK_VERSION_DEFAULT = '_rpnpy'
TDPACK_VERSION_DEFAULT = '*'


class TDPACKError(Exception):
    """
    General TDPACK module error/exception
    """
    pass


def checkTDPACKlibPath(libfile):
    """
    Return first matched filename for libfile wildcard
    Return None if no match
    """
    import os
    import glob
    LIBPATH_ALL = glob.glob(libfile)
    if len(LIBPATH_ALL) > 0:
        if os.path.isfile(LIBPATH_ALL[0]):
            return LIBPATH_ALL[0]
    return None


def loadTDPACKlib(tdpack_version=None):
    """
    Import libtdpack.so using ctypes

    Args:
       tdpack_version (str): libtdpack version number to load
                          Default: RPNPY_TDPACK_VERSION Env.Var.
                                   TDPACK_VERSION_DEFAULT if not RPNPY_TDPACK_VERSION
    Returns:
       (TDPACK_VERSION, TDPACK_LIBPATH, libtdpack)
       where:
       TDPACK_VERSION (str)  : loaded libtdpack version
       TDPACK_LIBPATH (str)  : path to loaded libtdpack shared lib
       libtdpack      (CDLL) : ctypes library object for libtdpack.so
       
    Library 'libtdpackVERSION.so' is searched into the Env.Var. paths:
       PYTHONPATH, EC_LD_LIBRARY_PATH, LD_LIBRARY_PATH
    """
    import os
    import ctypes as ct
    ## import numpy  as np
    ## import numpy.ctypeslib as npct

    if tdpack_version is None:
        TDPACK_VERSION = os.getenv('RPNPY_TDPACK_VERSION',
                                    TDPACK_VERSION_DEFAULT).strip()
    else:
        TDPACK_VERSION = tdpack_version
    tdpack_libfile = 'libtdpack' + TDPACK_VERSION.strip() + '.so'

    pylibpath   = os.getenv('PYTHONPATH','').split(':')
    ldlibpath   = os.getenv('LD_LIBRARY_PATH','').split(':')
    eclibpath   = os.getenv('EC_LD_LIBRARY_PATH','').split()
    TDPACK_LIBPATH = checkTDPACKlibPath(tdpack_libfile)
    if not TDPACK_LIBPATH:
        for path in pylibpath + ldlibpath + eclibpath:
            TDPACK_LIBPATH = checkTDPACKlibPath(os.path.join(path.strip(), tdpack_libfile))
            if TDPACK_LIBPATH:
                break

    if not TDPACK_LIBPATH:
        raise IOError(-1, 'Failed to find libtdpack.so: ', tdpack_libfile)

    TDPACK_LIBPATH = os.path.abspath(TDPACK_LIBPATH)
    libtdpack = None
    try:
        libtdpack = ct.cdll.LoadLibrary(TDPACK_LIBPATH)
        #libtdpack = np.ctypeslib.load_library(tdpack_libfile, TDPACK_LIBPATH)
    except IOError:
        raise IOError('ERROR: cannot load libtdpack shared version: ' +
                      TDPACK_VERSION)
    return (TDPACK_VERSION, TDPACK_LIBPATH, libtdpack)

(TDPACK_VERSION, TDPACK_LIBPATH, libtdpack) = loadTDPACKlib()


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# -*- Mode: C; tab-width: 4; indent-tabs-mode: nil -*-
# vim: set expandtab ts=4 sw=4:
# kate: space-indent on; indent-mode cstyle; indent-width 4; mixedindent off;
