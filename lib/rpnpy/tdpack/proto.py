#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Stephane Chamberland <stephane.chamberland@ec.gc.ca>
# Copyright: LGPL 2.1

"""
Module tdpack is a ctypes import of tdpack's library (libtdpack.so)

The tdpack.proto python module includes ctypes prototypes for many
tdpack's libtdpack functions.

Warning:
    Please use with caution.
    The functions in this module are actual C/Fortran funtions and must thus
    be called as such with appropriate argument typing and dereferencing.
    It is highly advised in a python program to prefer the use of the
    python wrapper found in
    * rpnpy.tdpack.base

Notes:
    The functions described below are a very close ''port'' from the original
    [[Tdpack]] package.<br>
    You may want to refer to the [[Tdpack]] documentation for more details.

See Also:
    rpnpy.tdpack.base
    rpnpy.tdpack.const

Details:
    See Source Code

##DETAILS_START
== Functions C/Fortran Prototypes ==

<source lang="python">
 f_mesahr(hr, es, tt, ps, swph, ni, nk, n)
    Calculate relative humidity from dew point depressions,
    temperature and pressure.

    Proto:

    Args:
       hr       (float ptr) relative humidity (percentage) (O)
       es       (float ptr) (t-td) in K (I)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mhraes
       f_mesahu
       f_mhuahr


 f_mhraes(es, hr, tt, ps, swph, ni, nk, n)
    Calculate dew point depressions from relative humidity,
    temperature and pressure

    Proto:

    Args:
       es       (float ptr) (t-td) in K (O)
       hr       (float ptr) relative humidity (percentage) (I)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mesahu
       f_mhrahu
       f_mhuaes


 f_mesahu(hu, es, tt, ps, swph, ni, nk, n)
    Calculate specific humidity from dew point depressions,
    temperature and pressure

    Proto:

    Args:
       hu       (float ptr) specific humidity in kg/kg (O)
       es       (float ptr) (t-td) in K (I)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mhuaes


f_mhuaes(es, hu, tt, ps, swph, ni, nk, n)
    Calculate dew point depressions from specific humidity,
    temperature and pressure

    Proto:

    Args:
       es       (float ptr) (t-td) in K (O)
       hu       (float ptr) specific humidity in kg/kg (I)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mhuaes


 f_mhrahu(hu, hr, tt, ps, swph, ni, nk, n)
    Calculate specific humidity from relative humidity,
    temperature and pressure

    Proto:

    Args:
       hu       (float ptr) specific humidity in kg/kg (O)
       hr       (float ptr) relative humidity (percentage) (I)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mhuahr


 f_mhuahr(hr, hu, tt, ps, swph, ni, nk, n)
    Calculate relative humidity from specific humidity,
    temperature and pressure

    Proto:

    Args:
       hr       (float ptr) relative humidity (percentage) (O)
       hu       (float ptr) specific humidity in kg/kg (I)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mhrahu


 f_mfodla(de, tt, ni, nk, n)
    Calculate the derivative according to t of 'ln(ew)'
    (water phase considered only for all temperatures)

    Proto:

    Args:
       de       (float ptr) derivative on LN(EW) (O)
       tt       (float ptr) temperature in K (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfodle


 f_mfodle(de, tt, ni, nk, n)
    Calculate the derivative of ln(ew) or ln(ei)
    w.r.t. tt for water or ice phase

    Proto:

    Args:
       de       (float ptr) derivative on LN(EW) (O)
       tt       (float ptr) temperature in K (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfodla


 f_mfotvt(tv, tt, hu, ni, nk, n)
    Calculate virtual temperature tv
    from temperature tt and specific humidity hu

    Proto:

    Args:
       vt       (float ptr) virtual temperature in K (O)
       tt       (float ptr) temperature in K (I)
       hu       (float ptr) specific humidity in kg/kg (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfottv
       f_mfottvh
       f_mfotvht

 f_mfottv(tt, tv, hu, ni, nk, n)
    Calculate temperature tt
    from virtual temperature tv and specific humidity hu

    Proto:

    Args:
       tt       (float ptr) temperature in K (O)
       vt       (float ptr) virtual temperature in K (I)
       hu       (float ptr) specific humidity in kg/kg (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfotvt
       f_mfotvht
       f_mfottvh


 f_mfotvht(tv, tt, hu, qh, ni, nk, n)
    Calculate virtual temperature tv
    from temperature tt and specific humidity hu
    and specific mass of hydrometeors qh.
    Note - The virtual temperature here is the one that accounts
    for the vapor and the hydrometeors.

    Proto:

    Args:
       vt       (float ptr) virtual temperature in K (O)
       tt       (float ptr) temperature in K (I)
       hu       (float ptr) specific humidity in kg/kg (I)
       qh       (float ptr) specific mass of hydrometeors in kg/kg (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfottv
       f_mfottvh
       f_mfotvt


 f_mfottvh(tt, tv, hu, qh, ni, nk, n)
    Calculate temperature tt
    from virtual temperature tv and specific humidity hu
    and specific mass of hydrometeors qh.
    Note - The virtual temperature here is the one that accounts
    for the vapor and the hydrometeors.

    Proto:

    Args:
       tt       (float ptr) temperature in K (O)
       vt       (float ptr) virtual temperature in K (I)
       hu       (float ptr) specific humidity in kg/kg (I)
       qh       (float ptr) specific mass of hydrometeors in kg/kg (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfotvt
       f_mfotvht
       f_mfottv


f_mfodqa(dq, tt, ps, ni, nk, n)
    Calculate the derivative of QSAT(saturation specific humidity)
    according to T (water phase considered only for all temperatures)

    Proto:

    Args:
       dq       (float ptr) derivative of QSAT (saturation specific humidity)  (O)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfodqs


f_mfodqs(dq, tt, ps, ni, nk, n)
    Calculate the derivative of QSAT(saturation specific humidity)
    according to T (water and ice phase considered according to temperature)

    Proto:

    Args:
       dq       (float ptr) derivative of QSAT (saturation specific humidity) (O)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfodqa


f_mfoqsa(qs, tt, ps, ni, nk, n)
    Calculate specific humidity at saturation (water only) in kg/kg

    Proto:

    Args:
       qs       (float ptr) specific humidity at saturation in kg/kg (O)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfoqst

f_mfoqst(qs, tt, ps, ni, nk, n)
    Calculate specific humidity at saturation in kg/kg

    Proto:

    Args:
       qs       (float ptr) specific humidity at saturation in kg/kg (O)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfoqsa

f_mfoqfe(hu, ee, ps, ni, nk, n)
    Calculate specific humidity from vapour pressure and pressure

    Proto:

    Args:
       hu       (float ptr) specific humidity in kg/kg (O)
       ee       (float ptr) vapour pressure in Pa (I)
       ps       (float ptr) pressure in Pa (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfoqfe

f_mfoefq(ee, hu, ps, ni, nk, n)
    Calculate vapour pressure from specific humidity and pressure

    Proto:

    Args:
       ee       (float ptr) vapour pressure in Pa (O)
       hu       (float ptr) specific humidity in kg/kg (I)
       ps       (float ptr) pressure in Pa (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfoqfe

 f_mfoeic(ei, tt, ni, nk, n)
    Calculate saturated vapour pressure (ice only) from temperature

    Proto:

    Args:
       ei       (float ptr) saturated vapour pressure in Pa (O)
       tt       (float ptr) temperature in K (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfoew
       f_mfoewa

 f_mfoew(ew, tt, ni, nk, n)
    Calculate saturated vapour pressure (water and ice) from temperature

    Proto:

    Args:
       ew       (float ptr) saturated vapour pressure in Pa (O)
       tt       (float ptr) temperature in K (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfoewa
       f_mfoeic

 f_mfoewa(ew, tt, ni, nk, n)
    Calculate saturated vapour pressure (water only) from temperature

    Proto:

    Args:
       ew       (float ptr) saturated vapour pressure in Pa (O)
       tt       (float ptr) temperature in K (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mfoew
       f_mfoeic


 f_mfohr(hr, hu, tt, ps, ni, nk, n, satuco)
    Calculate relative humidity from specific humidity,
    temperature and pressure

    Proto:

    Args:
       hr       (float ptr) relative humidity (percentage) (O)
       hu       (float ptr) specific humidity in kg/kg (I)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
       satuco   (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
    Returns:
       None
    See Also:
       f_mhuahr
       f_mhrahu

 f_modhui(hu, tt, swph, ni, nk, n)
    Recalculate recalculate the specific humidity over 300MB.
    by using the zeroth order interpolation
    and keeping one of the following constant:
    A) The relative humidity when the temperature decreases
       to simulate what happens below the tropopause.
    or
    B) The specific humidity when the temperature increases
       to simulate what happens above the tropopause.

    Proto:

    Args:
       hu       (float ptr) specific humidity in kg/kg (O) (?I/O?)
       tt       (float ptr) temperature in K (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:

 f_mthtaw3(tw, hu, tt, ps, swph, swth, ni, nk, n)
    Calculate TW or THETAW (according to the value SWTT)
    from specific humidity, temperature and pressure

    Proto:

    Args:
       tw       (float ptr) TW or ThetaW (according to the value SWTT) in K (O)
       hu       (float ptr) specific humidity in kg/kg (I) (?I/O?)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       swth     (int) (I)
                1 (.true.)  calculate thetaw
                0 (.false.) calculate tw
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mthtaw4

 f_mthtaw4(tw, hu, tt, ps, swph, swth, ti, ni, nk, n)
    Calculate TW or THETAW (according to the value SWTH)
    from specific humidity, temperature and pressure

    Proto:

    Args:
       tw       (float ptr) TW or ThetaW (according to the value SWTH) in K (O)
       hu       (float ptr) specific humidity in kg/kg (I) (?I/O?)
       tt       (float ptr) temperature in K (I)
       ps       (float ptr) pressure in Pa (I)
       swph     (int) (I)
                1 (.true.) to consider water and ice phase 
                0 (.false.) to consider water phase only
       swth     (int) (I)
                1 (.true.)  calculate thetaw
                0 (.false.) calculate tw
       ti       (float) : temperature in K at which we start calculating
                          latent heat of sublimation (I)
                          if swph=false, ti is n/a
                          ti must be <= TRPL
       ni       (int) : horizontal dimension (I)
       nk       (int) : vertical dimension (I)
       n        (int) : number of treated points (I)
    Returns:
       None
    See Also:
       f_mthtaw3

</source>
##DETAILS_END
"""

#? ?? 0000000000004520 T mfottv2_
#? ?? 0000000000004960 T mfottvh2_
#? ?? 000000000056a0 T modhui3_

## 0000000000006430 T schal_
#? ?? 0000000000006510 T sesahr3_
#? ?? 0000000000006550 T sesahu3_
#? ?? 00000000000065b0 T sfodla_
#? ?? 00000000000065d0 T sfodle_
#? ?? 00000000000065f0 T sfodqa_
#? ?? 0000000000006620 T sfodqs_
#? ?? 0000000000006650 T sfoefq_
#? ?? 0000000000006670 T sfoew_
#? ?? 0000000000006690 T sfoewa_
#? ?? 00000000000066b0 T sfohr_
## 00000000000066d0 T sfohra_
## 00000000000066f0 T sfols_
## 0000000000006710 T sfolv_
## 0000000000006730 T sfopop_
## 0000000000006750 T sfopot_
#? ?? 0000000000006770 T sfoqfe_
#? ?? 0000000000006790 T sfoqsa_
#? ?? 00000000000067b0 T sfoqst_
#? ?? 00000000000067d0 T sfottv_
#? ?? 00000000000067f0 T sfotvt_
## 0000000000006810 T sgamash_
## 0000000000006990 T sgamasp_
## 0000000000006b30 T sgamatd_
#? ?? 0000000000006bd0 T shraes3_
#? ?? 0000000000006c10 T shrahu3_
#? ?? 0000000000006c80 T shuaes3_
#? ?? 0000000000006d40 T shuahr3_
## 0000000000006d60 T stetae_
#? ?? 0000000000006f00 T sthtaw3_
#? ?? 0000000000007290 T sthtaw4_
## 00000000000074b0 T sttlcl_

import ctypes as _ct
import numpy  as _np
import numpy.ctypeslib as _npc

from . import libtdpack
#from . import const as _cst

libtdpack.mesahr3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mesahr = libtdpack.mesahr3_

libtdpack.mesahu3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mesahu = libtdpack.mesahu3_

libtdpack.mhraes3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mhraes = libtdpack.mhraes3_

libtdpack.mhrahu3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mhrahu = libtdpack.mhrahu3_

libtdpack.mhuaes3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mhuaes = libtdpack.mhuaes3_

libtdpack.mhuahr3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mhuahr = libtdpack.mhuahr3_

libtdpack.mfodla_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfodla = libtdpack.mfodla_

libtdpack.mfodle_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfodle = libtdpack.mfodle_

libtdpack.mfotvt_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfotvt = libtdpack.mfotvt_

libtdpack.mfottv_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfottv = libtdpack.mfottv_

libtdpack.mfotvht_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfotvht = libtdpack.mfotvht_

libtdpack.mfottvh_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfottvh = libtdpack.mfottvh_

libtdpack.mfodqa3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfodqa = libtdpack.mfodqa3_

libtdpack.mfodqs3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfodqs = libtdpack.mfodqs3_

libtdpack.mfoqsa3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfoqsa = libtdpack.mfoqsa3_

libtdpack.mfoqst3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfoqst = libtdpack.mfoqst3_

libtdpack.mfoqfe3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfoqfe = libtdpack.mfoqfe3_

libtdpack.mfoefq3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfoefq = libtdpack.mfoefq3_

libtdpack.mfoeic_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfoeic = libtdpack.mfoeic_

libtdpack.mfoew_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfoew = libtdpack.mfoew_

libtdpack.mfoewa_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfoewa = libtdpack.mfoewa_

libtdpack.mfohr4_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_mfohr = libtdpack.mfohr4_

libtdpack.modhui4_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack..restype  = _ct.c_int
f_modhui = libtdpack.modhui4_

libtdpack.mthtaw3_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_int), 
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack.mthtaw3_.restype  = _ct.c_int
f_mthtaw3 = libtdpack.mthtaw3_

libtdpack.mthtaw4_.argtypes = (
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _npc.ndpointer(dtype=_np.float32),
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int),
    _ct.POINTER(_ct.c_float),
    _ct.POINTER(_ct.c_int), 
    _ct.POINTER(_ct.c_int), _ct.POINTER(_ct.c_int))
## libtdpack.mthtaw4_.restype  = _ct.c_int
f_mthtaw4 = libtdpack.mthtaw4_
