#!/usr/bin/env python
# . s.ssmuse.dot /ssm/net/hpcs/201402/02/base /ssm/net/hpcs/201402/02/intel13sp1u2 /ssm/net/rpn/libs/15.2

"""
 Module librmn is a ctypes import of librmnshared.so
 
 The librmn python module includes
 - python wrapper to main librmn's C functions
 - helper functions
 - prototypes for many librmn's C functions
 - pre-defined constants
 - along with comprenhensive inline documentation

 See also:
 help(librmn.proto)
 help(librmn.const)
 help(librmn.base)
 help(librmn.fstd98)
 help(librmn.interp)
 help(librmn.grids)

 @author: Stephane Chamberland <stephane.chamberland@ec.gc.ca>
"""

#TODO: burp
#TODO: rdiag
#TODO: vgrid
#TODO: modelutil's tdpack
#TODO: modelutil's ???

from rpnpy.version import *

__SUBMODULES__ = ['proto','const','base','fstd98','interp','llacar','grids']
__all__ = ['loadRMNlib','librmn','RMN_VERSION','RMN_LIBPATH','RMNError'] + __SUBMODULES__

RMN_VERSION_DEFAULT = '_015.2'

class RMNError(Exception):
    pass

def loadRMNlib(rmn_version=None):
    """Import librmnshared using ctypes

    Args:
       rmn_version (str): librmnshared version number to load
                          Default: RPNPY_RMN_VERSION Env.Var.
                                   RMN_VERSION_DEFAULT if not RPNPY_RMN_VERSION
    Returns:
       (RMN_VERSION, RMN_LIBPATH, librmn)
       where:
       RMN_VERSION (str)  : loaded librmn version
       RMN_LIBPATH (str)  : path to loaded librmn shared lib
       librmn      (CDLL) : ctypes library object for librmn.so
       
    Library 'librmnsharedVERSION.so' is searched into the Env.Var. paths:
       PYTHONPATH, EC_LD_LIBRARY_PATH, LD_LIBRARY_PATH
    """
    import os
    import ctypes as ct
    ## import numpy  as np
    ## import numpy.ctypeslib as npct

    if rmn_version is None:
        RMN_VERSION = os.getenv('RPNPY_RMN_VERSION',RMN_VERSION_DEFAULT).strip()
    else:
        RMN_VERSION = rmn_version
    rmn_libfile = 'librmnshared'+RMN_VERSION.strip()+'.so'

    pylibpath   = os.getenv('PYTHONPATH').split(':')
    ldlibpath   = os.getenv('LD_LIBRARY_PATH').split(':')
    eclibpath   = os.getenv('EC_LD_LIBRARY_PATH').split()
    RMN_LIBPATH = rmn_libfile
    if not os.path.exists(RMN_LIBPATH):
        for path in pylibpath + eclibpath + eclibpath:
            RMN_LIBPATH = os.path.join(path.strip(),rmn_libfile)
            if os.path.exists(RMN_LIBPATH):
                break
            else:
                RMN_LIBPATH = None

    if not RMN_LIBPATH:
        raise IOError,(-1,'Failed to find librmn.so: ',rmn_libfile)

    librmn = None
    try:
        librmn = ct.cdll.LoadLibrary(RMN_LIBPATH)
        #librmn = np.ctypeslib.load_library(rmn_libfile,RMN_LIBPATH)
    except IOError:
        raise IOError('ERROR: cannot load librmn shared version: '+RMN_VERSION)
    return (RMN_VERSION, RMN_LIBPATH, librmn)

(RMN_VERSION,RMN_LIBPATH,librmn) = loadRMNlib()
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# -*- Mode: C; tab-width: 4; indent-tabs-mode: nil -*-
# vim: set expandtab ts=4 sw=4:
# kate: space-indent on; indent-mode cstyle; indent-width 4; mixedindent off;