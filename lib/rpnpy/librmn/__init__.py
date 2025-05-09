#!/usr/bin/env python
# -*- coding: utf-8 -*-
# . s.ssmuse.dot /ssm/net/hpcs/201402/02/base \
#                /ssm/net/hpcs/201402/02/intel13sp1u2 /ssm/net/rpn/libs/15.2
# Author: Stephane Chamberland <stephane.chamberland@canada.ca>
# Copyright: LGPL 2.1
"""
 Module librmn is a ctypes import of librmn.so
 
 The librmn python module includes
 - python wrapper to main librmn's C functions
 - helper functions
 - prototypes for many librmn's C functions
 - pre-defined constants
 - along with comprenhensive inline documentation

 See also:
     rpnpy.librmn.proto
     rpnpy.librmn.const
     rpnpy.librmn.base
     rpnpy.librmn.fstd98
     rpnpy.librmn.interp
     rpnpy.librmn.grids
     rpnpy.librmn.proto_burp
     rpnpy.librmn.burp_const
     rpnpy.librmn.burp
     rpnpy.librmn.proto_app
     rpnpy.librmn.app_const
     rpnpy.librmn.app
"""

from rpnpy.version import *

__SUBMODULES__ = ['proto', 'const', 'base', 'fstd98', 'interp', 'grids',
                  'proto_burp', 'burp_const', 'burp',
                  'proto_app', 'app_const', 'app']
__all__ = ['loadRMNlib', 'librmn', 'RMN_VERSION', 'RMN_LIBPATH',
           'RMNError'] + __SUBMODULES__

## RMN_VERSION_DEFAULT = '_rpnpy'
RMN_VERSION_DEFAULT = '*'

class RMNError(Exception):
    """
    General RMN module error/exception
    """
    pass

def checkRMNlibPath(rmn_libfile):
    """
    Return first matched filename for rmn_libfile wildcard
    Return None if no match
    """
    import os
    import glob
    RMN_LIBPATH_ALL = glob.glob(rmn_libfile)
    if len(RMN_LIBPATH_ALL) > 0:
        if os.path.isfile(RMN_LIBPATH_ALL[0]):
            return RMN_LIBPATH_ALL[0]
    return None

def loadRMNlib(rmn_version=None):
    """
    Import librmn shared using ctypes

    Args:
       rmn_version (str): librmn shared version number to load
                          Default: RPNPY_RMN_VERSION Env.Var.
                                   RMN_VERSION_DEFAULT if not RPNPY_RMN_VERSION
    Returns:
       (RMN_VERSION, RMN_LIBPATH, librmn)
       where:
       RMN_VERSION (str)  : loaded librmn version
       RMN_LIBPATH (str)  : path to loaded librmn shared lib
       librmn      (CDLL) : ctypes library object for librmn.so

    Library 'librmn.so.VERSION' is searched into the following Env.Var. paths (in order):
      RPNPY_RMN_PATH
      Python environment path (sys.prefix / lib)
      LD_LIBRARY_PATH
    """
    import os
    import sys
    import ctypes as ct
    import logging
    if rmn_version is None:
        RMN_VERSION = os.getenv('RPNPY_RMN_VERSION',
                                RMN_VERSION_DEFAULT).strip()
    else:
        RMN_VERSION = rmn_version
    if (RMN_VERSION.strip() == '' or RMN_VERSION.strip() == '*'):
        rmn_libfile = 'librmn.so'
    else:
        rmn_libfile = 'librmn.so.' + RMN_VERSION.strip()

    # A path specified through the env by the user
    RMN_PATH = os.getenv('RPNPY_RMN_PATH')
    userlibpath = [RMN_PATH] if RMN_PATH else []
    # Main system or environment (conda for example) library path
    envlibpath  = [os.path.join(sys.prefix, 'lib')]
    # pylibpath   = os.getenv('PYTHONPATH','').split(':')
    ldlibpath   = os.getenv('LD_LIBRARY_PATH','').split(':')
    # eclibpath   = os.getenv('EC_LD_LIBRARY_PATH','').split()
    RMN_LIBPATH = checkRMNlibPath(rmn_libfile)
    if not RMN_LIBPATH:
        for path in userlibpath + envlibpath + ldlibpath: # + pylibpath + ldlibpath + eclibpath:
            RMN_LIBPATH = checkRMNlibPath(os.path.join(path.strip(), rmn_libfile))
            if RMN_LIBPATH:
                break

    if not RMN_LIBPATH:
        raise IOError(-1, 'Failed to find librmn.so: ', rmn_libfile)

    librmn = None
    try:
        logging.debug('Loading librmn.so from: %s', RMN_LIBPATH)
        librmn = ct.cdll.LoadLibrary(RMN_LIBPATH)
        #librmn = np.ctypeslib.load_library(rmn_libfile, RMN_LIBPATH)
    except IOError as e:
        raise IOError('ERROR: cannot load librmn shared version: ' +
                      RMN_VERSION, e)
    return (RMN_VERSION, RMN_LIBPATH, librmn)

(RMN_VERSION, RMN_LIBPATH, librmn) = loadRMNlib()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# -*- Mode: C; tab-width: 4; indent-tabs-mode: nil -*-
# vim: set expandtab ts=4 sw=4:
# kate: space-indent on; indent-mode cstyle; indent-width 4; mixedindent off;
