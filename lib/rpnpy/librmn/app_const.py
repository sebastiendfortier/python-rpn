#!/usr/bin/env python
# -*- coding: utf-8 -*-
# . s.ssmuse.dot /ssm/net/hpcs/201402/02/base \
#                /ssm/net/hpcs/201402/02/intel13sp1u2 /ssm/net/rpn/libs/15.2
# Author: Stephane Chamberland <stephane.chamberland@canada.ca>
# Copyright: LGPL 2.1

"""
Module libapp.const defines a set of helper constants to make code
using the libapp module more readable.

Notes:
    This module is a very close ''port'' from the original
    [[libapp]]'s package.<br>
    You may want to refer to the [[libapp/base]]
    documentation for more details.

See Also:
    rpnpy.librmn.app
    rpnpy.librmn.proto_app

Details:
    See Source Code
    https://gitlab.science.gc.ca/RPN-SI/App/blob/master/src/App.h
"""
import numpy  as _np

##DETAILS_START
#== App Constants Details ==
#<source lang=python>

APP_TRUE   = 1
APP_FALSE  = 0

APP_COLOR_BLINK      = "\x1b[5m"
APP_COLOR_BLACK      = "\x1b[0;30m"
APP_COLOR_RED        = "\x1b[0;31m"
APP_COLOR_GREEN      = "\x1b[0;32m"
APP_COLOR_LIGHTGREEN = "\x1b[1;32m"
APP_COLOR_ORANGE     = "\x1b[33m" 
APP_COLOR_YELLOW     = "\x1b[1m\x1b[33m"
APP_COLOR_BLUE       = "\x1b[0;34m"
APP_COLOR_MAGENTA    = "\x1b[0;35m"
APP_COLOR_CYAN       = "\x1b[0;36m"
APP_COLOR_LIGHTCYAN  = "\x1b[1m\x1b[36m"
APP_COLOR_GRAY       = "\x1b[0;37m"
APP_COLOR_RESET      = "\x1b[0m"
APP_MASTER    = 0
APP_THREAD    = 1

APP_ERRORSIZE = 2048
APP_BUFMAX    = 32768               ## Maximum input buffer length
APP_LISTMAX   = 4096                ## Maximum number of items in a flag list
APP_SEED      = 1049731793          ## Initial FIXED seed
APP_LIBSMAX   = 64                  ## Maximum number of libraries

APP_NOARGSFLAG = 0x00               ## No flag specified
APP_NOARGSFAIL = 0x01               ## Fail if no arguments are specified
APP_ARGSLOG    = 0x02               ## Use log flag
APP_ARGSLANG   = 0x04               ## Multilingual app
APP_ARGSSEED   = 0x08               ## Use seed flag
APP_ARGSTHREAD = 0x10               ## Use thread flag
APP_ARGSTMPDIR = 0x20               ## Use tmp dir

##ifdef __xlC__
##   define APP_ONCE    ((1)<<3)
##else
##   define APP_ONCE    ((__COUNTER__+1)<<3)
##endif
## APP_MAXONCE = 1024

## TApp_Lib
APP_MAIN = 0
APP_LIBRMN = 1
APP_LIBFST = 2
APP_LIBWB = 3
APP_LIBGMM = 4
APP_LIBVGRID = 5
APP_LIBINTERPV = 6
APP_LIBGEOREF = 7
APP_LIBRPNMPI = 8
APP_LIBIRIS = 9
APP_LIBIO = 10
APP_LIBMDLUTIL = 11
APP_LIBGEMDYN = 12
APP_LIBRPNPHY = 13
APP_LIBMIDAS = 14
APP_LIBEER = 15

APP_LOGIDMIN = APP_MAIN
APP_LOGIDMAX = APP_LIBEER


## TApp_LogLevel
APP_VERBATIM = -1
APP_ALWAYS = 0
APP_FATAL = 1
APP_SYSTEM = 2
APP_ERROR = 3
APP_WARNING = 4
APP_INFO = 5
APP_TRIVIAL = 6
APP_DEBUG = 7
APP_EXTRA = 8
APP_QUIET = 9

APP_LOGLEVELMIN = APP_VERBATIM
APP_LOGLEVELMAX = APP_QUIET

APP_LOGLEVEL_NAMES = {
    APP_VERBATIM : 'VERBATIM',
    APP_ALWAYS : 'ALWAYS',
    APP_FATAL : 'FATAL',
    APP_SYSTEM : 'SYSTEM',
    APP_ERROR : 'ERROR',
    APP_WARNING : 'WARNING',
    APP_INFO : 'INFO',
    APP_TRIVIAL : 'TRIVIAL',
    APP_DEBUG : 'DEBUG',
    APP_EXTRA : 'EXTRA',
    APP_QUIET : 'QUIET'
   }
APP_LOGLEVEL_NAMES_INV = dict([(v, k) for k, v in APP_LOGLEVEL_NAMES.items()])


## TApp_LogTime
APP_NODATE = 0
APP_DATETIME = 1
APP_TIME = 2
APP_SECOND = 3
APP_MSECOND = 4

## TApp_State
APP_STOP = 0
APP_RUN = 1
APP_DONE = 2

## TApp_Type
APP_NIL = 0x0
APP_FLAG = 0x01
APP_CHAR = 0x02
APP_UINT32 = 0x04
APP_INT32 = 0x06
APP_UINT64 = 0x08
APP_INT64 = 0x0A
APP_FLOAT32 = 0x0C
APP_FLOAT64 = 0x0E

## TApp_Lang
APP_FR = 0x0
APP_EN = 0x01

## TApp_RetCode
APP_OK = 1
APP_ERR = 0

## TApp_Affinity
APP_AFFINITY_NONE = 0
APP_AFFINITY_COMPACT = 1
APP_AFFINITY_SCATTER = 2
APP_AFFINITY_SOCKET = 3

#</source>
##DETAILS_END


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# -*- Mode: C; tab-width: 4; indent-tabs-mode: nil -*-
# vim: set expandtab ts=4 sw=4:
# kate: space-indent on; indent-mode cstyle; indent-width 4; mixedindent off;
