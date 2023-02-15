#!/usr/bin/env python
# -*- coding: utf-8 -*-
# . s.ssmuse.dot /ssm/net/hpcs/201402/02/base \
#                /ssm/net/hpcs/201402/02/intel13sp1u2 /ssm/net/rpn/libs/15.2
# Author: Stephane Chamberland <stephane.chamberland@canada.ca>
# Copyright: LGPL 2.1

"""
Module librmn.proto_app is a ctypes import of libApp function found in librmn.so

The librmn.proto_app python module includes ctypes prototypes for many
libApp C functions

Warning:
    Please use with caution.
    The functions in this module are actual C funtions and
    must thus be called as such with appropriate argument typing and
    dereferencing.
    It is highly advised in a python program to prefer the use of the
    python wrapper found in
    * rpnpy.librmn.app
    * rpnpy.librmn.app_const

Notes:
    The functions described below are a very close ''port'' from the original
    [[libApp]]'s functions.<br>
    You may want to refer to the [[LibApp]]
    documentation for more details.

See Also:
    rpnpy.librmn.app
    rpnpy.librmn.app_const

Details:
    See Source Code

##DETAILS_START
== External C Functions ==
<source lang="python">

c_App_LogLevelNo(level)
        Set new log level for the Main app
        Proto:
           int App_LogLevelNo(TApp_LogLevel level);
        Args:
           level (int): (I) new log level
        Returns:
           int, previous leg level of MAIN logger

c_Lib_LogLevelNo(libId, level)
        Set new log level for the specified libId
        Proto:
           int Lib_LogLevelNo(TApp_Lib libId, TApp_LogLevel level);
        Args:
           libId (int): (I) numberId of the lib to set the log level for
           level (int): (I) new log level
        Returns:
           int, previous leg level of libId logger

</source>
##DETAILS_END

"""
import ctypes as _ct
import numpy  as _np
import numpy.ctypeslib as _npc

from . import librmn

# int   App_LogLevelNo(TApp_LogLevel Val);
librmn.App_LogLevelNo.argtypes = (_ct.c_int, )
librmn.App_LogLevelNo.restype  = _ct.c_int
c_App_LogLevelNo = librmn.App_LogLevelNo

# int   Lib_LogLevelNo(TApp_Lib Lib,TApp_LogLevel Val);
librmn.Lib_LogLevelNo.argtypes = (_ct.c_int, )
librmn.Lib_LogLevelNo.restype  = _ct.c_int
c_Lib_LogLevelNo = librmn.Lib_LogLevelNo


## #define App_Log(LEVEL, ...) Lib_Log(APP_MAIN,LEVEL,__VA_ARGS__)

## TApp *App_Init(int Type,char* Name,char* Version,char* Desc,char* Stamp);
## void  App_LibRegister(TApp_Lib Lib,char *Version);
## void  App_Free(void);
## void  App_Start(void);
## int   App_End(int Status);
## void  Lib_Log(TApp_Lib Lib,TApp_LogLevel Level,const char *Format,...);
## int   Lib_LogLevel(TApp_Lib Lib,char *Val);
## int   Lib_LogLevelNo(TApp_Lib Lib,TApp_LogLevel Val);
## int   App_LogLevel(char *Val);
## int   App_LogLevelNo(TApp_LogLevel Val);
## int   App_ToleranceLevel(char *Val);
## int   App_ToleranceNo(TApp_LogLevel Val);
## void  App_LogOpen(void);
## void  App_LogClose(void);
## int   App_LogTime(char *Val);
## void  App_Progress(float Percent,const char *Format,...);
## int   App_ParseArgs(TApp_Arg *AArgs,int argc,char *argv[],int Flags);
## int   App_ParseInput(void *Def,char *File,TApp_InputParseProc *ParseProc);
## int   App_ParseBool(char *Param,char *Value,char *Var);
## int   App_ParseDate(char *Param,char *Value,time_t *Var);
## int   App_ParseDateSplit(char *Param,char *Value,int *Year,int *Month,int *Day,int *Hour,int *Min);
## int   App_ParseCoords(char *Param,char *Value,double *Lat,double *Lon,int Index);
## void  App_SeedInit(void);
## char* App_ErrorGet(void);
## int   App_ThreadPlace(void);
## void  App_Trap(int Signal);
## int   App_IsDone(void); 
## int   App_IsMPI(void);
## int   App_IsOMP(void);
## int   App_IsSingleNode(void);
## int   App_IsAloneNode(void);
## int   App_NodeGroup();
## int   App_NodePrint();


if __name__ == "__main__":
    print(str(c_fst_version()))

# -*- Mode: C; tab-width: 4; indent-tabs-mode: nil -*-
# vim: set expandtab ts=4 sw=4:
# kate: space-indent on; indent-mode cstyle; indent-width 4; mixedindent off;

