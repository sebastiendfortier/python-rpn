#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Stephane Chamberland <stephane.chamberland@ec.gc.ca>
# Copyright: LGPL 2.1

"""
Module librmn.app contains python wrapper to
main rpn/libs libApp C functions

Notes:
    The functions described below are a very close ''port'' from the original
    [[libApp]]'s functions package.<br>
    You may want to refer to the [[libapp]]
    documentation for more details.

See Also:
    rpnpy.librmn.app_const
    rpnpy.librmn.proto_app
    rpnpy.librmn
    rpnpy.vgrid
"""

import ctypes as _ct
import numpy  as _np

from rpnpy.librmn import proto_app as _ap
from rpnpy.librmn import app_const as _ac
from rpnpy.librmn import const as _rc
from rpnpy.librmn import RMNError

from rpnpy import integer_types as _integer_types
from rpnpy import C_WCHAR2CHAR as _C_WCHAR2CHAR
from rpnpy import C_CHAR2WCHAR as _C_CHAR2WCHAR
from rpnpy import C_MKSTR as _C_MKSTR

_C_TOINT = lambda x: (x if (type(x) != type(_ct.c_int())) else x.value)
_C_TOINT.__doc__ = 'lamda function to convert ctypes.c_int to python int'

APP2FST_LEVELS = {
    _ac.APP_VERBATIM : _rc.FSTOPI_MSG_DEBUG,
    _ac.APP_ALWAYS : _rc.FSTOPI_MSG_DEBUG,
    _ac.APP_FATAL : _rc.FSTOPI_MSG_FATAL,
    _ac.APP_SYSTEM : _rc.FSTOPI_MSG_SYSTEM,
    _ac.APP_ERROR : _rc.FSTOPI_MSG_ERROR,
    _ac.APP_WARNING : _rc.FSTOPI_MSG_WARNING,
    _ac.APP_INFO : _rc.FSTOPI_MSG_INFO,
    _ac.APP_TRIVIAL : _rc.FSTOPI_MSG_INFO,
    _ac.APP_DEBUG : _rc.FSTOPI_MSG_DEBUG,
    _ac.APP_EXTRA : _rc.FSTOPI_MSG_DEBUG,
    _ac.APP_QUIET : _rc.FSTOPI_MSG_CATAST
    }

def App_LevelFST2App(level):
    for k, v in APP2FST_LEVELS.items():
        if v == level:
            return k
        
def App_LevelApp2Fst(level):
    return APP2FST_LEVELS[level]

def App_LogLevelNo(level):
    """
    Set new log level for the Main app

    Args:
        level : new log level [int]
    Returns:
         int, previous leg level of MAIN logger
    Raises:
        TypeError  on wrong input arg types
        ValueError on invalid input arg value
        RMNBaseError on any other error

    Examples:
    >>> import os, sys
    >>> import rpnpy.librmn.all as rmn
    >>> level0 = rmn.App_LogLevelNo(rmn.APP_QUIET)
    >>> print("# Set Main from level={} '{}' to {} '{}'".format(level0, rmn.APP_LOGLEVEL_NAMES[level0], rmn.APP_QUIET, rmn.APP_LOGLEVEL_NAMES[rmn.APP_QUIET]))
    # Set Main from level=0 'ALWAYS' to 9 'QUIET'

    See also:
       fnom
       rpnpy.librmn.fstd98.fstopenall
       rpnpy.librmn.fstd98.fstcloseall
    """
    if not isinstance(level, _integer_types):
        raise TypeError("LogLevelNo: Expecting arg of type int, Got {0}"\
                        .format(type(level)))
    if level < _ac.APP_LOGLEVELMIN or level > _ac.APP_LOGLEVELMAX:
        raise ValueError("LogLevelNo: must provide a valid level: {0}".format(level))
    clevel = _ct.c_int(level)
    level = _ap.c_App_LogLevelNo(clevel)
    return level


def Lib_LogLevelNo(libId, level):
    """
    Set new log level for the specified libId

    Args:
        libId : numberId of the lib to set the log level for
        level : new log level [int]
    Returns:
         int, previous leg level of libId logger
    Raises:
        TypeError  on wrong input arg types
        ValueError on invalid input arg value
        RMNBaseError on any other error

    Examples:
    >>> import os, sys
    >>> import rpnpy.librmn.all as rmn
    >>> level0 = rmn.Lib_LogLevelNo(rmn.APP_LIBVGRID, rmn.APP_QUIET)
    >>> print("# Set libId={} from level={} '{}' to {} '{}'".format(rmn.APP_LIBVGRID, level0, rmn.APP_LOGLEVEL_NAMES[level0], rmn.APP_QUIET, rmn.APP_LOGLEVEL_NAMES[rmn.APP_QUIET]))
    # Set libId=5 from level=0 'ALWAYS' to 9 'QUIET'
    
    See also:
       fnom
       rpnpy.librmn.fstd98.fstopenall
       rpnpy.librmn.fstd98.fstcloseall
    """
    if not isinstance(level, _integer_types):
        raise TypeError("LogLevelNo: Expecting arg of type int, Got {0}"\
                        .format(type(level)))
    if level < _ac.APP_LOGLEVELMIN or level > _ac.APP_LOGLEVELMAX:
        raise ValueError("LogLevelNo: must provide a valid level: {0}".format(level))
    if libId < _ac.APP_LOGIDMIN or libId > _ac.APP_LOGIDMAX:
        raise ValueError("LogLevelNo: must provide a valid libid: {0}".format(libId))
    clibId = _ct.c_int(libId)
    clevel = _ct.c_int(level)
    level = _ap.c_Lib_LogLevelNo(clibId, clevel)
    return level


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# -*- Mode: C; tab-width: 4; indent-tabs-mode: nil -*-
# vim: set expandtab ts=4 sw=4:
# kate: space-indent on; indent-mode cstyle; indent-width 4; mixedindent off;
