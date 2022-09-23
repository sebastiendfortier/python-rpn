#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Stephane Chamberland <stephane.chamberland@ec.gc.ca>
# Copyright: LGPL 2.1

"""
Module tdpack.base contains python wrapper to main tdpack functions

Notes:
    The functions described below are a very close ''port'' from the original
    [[tdpack]]'s package.<br>
    You may want to refer to the [[Tdpack]] documentation for more details.

See Also:
    rpnpy.tdpack.proto
    rpnpy.tdpack.func
    rpnpy.tdpack.const
"""

import ctypes as _ct
import numpy  as _np
from rpnpy.tdpack import proto as _tp
## from rpnpy.tdpack import const as _tc
from rpnpy.librmn import RMNError

class TDPackError(RMNError):
    """
    General tdpack.base module error/exception

    To make your code handle errors in an elegant manner,
    you may want to catch that error with a 'try ... except' block.

    Examples:
    >>> import sys
    >>> import numpy as np
    >>> import rpnpy.tdpack.all as tdpack
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> try:
    ...     hr = tdpack.mhuahr(hu, tt, pp)
    ... except tdpack.TDPackError:
    ...     sys.stderr.write("There was a problem computing HR.")

    See also:
        rpnpy.librmn.RMNError
    """
    pass


def _checkArrayList(al, dtype=_np.float32):
    for a in al:
        if not isinstance(a, _np.ndarray):
            raise TypeError('Array must be a numpy ndarray')
        if not (a.flags['F_CONTIGUOUS'] and a.dtype == dtype):
            raise TypeError('Array must be F_CONTIGUOUS and of type {}'.format(dtype))
    for i in range(1,len(al)):
        if al[0].size != al[i].size:  #TODO: should we check shape instead?
            raise TypeError('All provided arrays must have the same size.')
    return (al[0].size, al[0].shape)


def _getOutArray(outArray, al, dtype=_np.float32):
    if outArray:
        al.append(outArray)
        size, shape = _checkArrayList(al, dtype=dtype)
    else:
        size, shape = _checkArrayList(al, dtype=dtype)
        outArray = _np.zeros(shape, dtype=dtype, order='F')
    cni, cnk, cnn = _ct.c_int(size), _ct.c_int(1), _ct.c_int(size)
    return cni, cnk, cnn, outArray


def mhuahr(hu, tt, pp, swph=False, outArray=None):
    """
    Compute relative humidity from specific humidity,
    temperature and pressure

    hr = tdpack.mhuahr(hu, tt, pp)
    hr = tdpack.mhuahr(hu, tt, pp, swph=True)
    hr = tdpack.mhuahr(hu, tt, pp, outArray=hr)

    Args:
        hu   : (numpy.ndarray, float32, F order) specific humidity in kg/kg
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        swph : True  - consider water and ice phase
               False - consider water phase only (default)
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        relative humidity (%)
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hr = tdpack.mhuahr(hu, tt, pp)

    See also:
        mhrahu
    """
    cni, cnk, cnn, hr = _getOutArray(outArray, [hu, tt, pp])
    ciswph = _ct.c_int(1 if swph else 0)
    _tp.f_mhuahr(hr, hu, tt, pp, _ct.byref(ciswph), _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return hr


def mhuaes(hu, tt, pp, swph=False, outArray=None):
    """
    Compute dew point depressions from specific humidity,
    temperature and pressure

    es = tdpack.mhuaes(hu, tt, pp)
    es = tdpack.mhuaes(hu, tt, pp, swph=True)
    es = tdpack.mhuaes(hu, tt, pp, outArray=es)

    Args:
        hu   : (numpy.ndarray, float32, F order) specific humidity in kg/kg
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        swph : True  - consider water and ice phase
               False - consider water phase only (default)
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        dew point depressions (t-td) in K 
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> es = tdpack.mhuaes(hu, tt, pp)

    See also:
        mesahu
    """
    cni, cnk, cnn, es = _getOutArray(outArray, [hu, tt, pp])
    ciswph = _ct.c_int(1 if swph else 0)
    _tp.f_mhuaes(es, hu, tt, pp, _ct.byref(ciswph), _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return es


def mhrahu(hr, tt, pp, swph=False, outArray=None):
    """
    Compute relative humidity from specific humidity,
    temperature and pressure

    hu = tdpack.mhrahu(hr, tt, pp)
    hu = tdpack.mhrahu(hr, tt, pp, swph=True)
    hu = tdpack.mhrahu(hr, tt, pp, outArray=hu)

    Args:
        hr   : (numpy.ndarray, float32, F order) relative humidity (%)
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        swph : True  - consider water and ice phase
               False - consider water phase only (default)
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        specific humidity [kg/kg]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> hr = np.array([0.1], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hu = tdpack.mhrahu(hr, tt, pp)

    See also:
        mhuahr
    """
    cni, cnk, cnn, hu = _getOutArray(outArray, [hr, tt, pp])
    ciswph = _ct.c_int(1 if swph else 0)
    _tp.f_mhrahu(hu, hr, tt, pp, _ct.byref(ciswph), _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return hu


def mhraes(hr, tt, pp, swph=False, outArray=None):
    """
    Compute dew point depressions from relative humidity,
    temperature and pressure

    es = tdpack.mhraes(hr, tt, pp)
    es = tdpack.mhraes(hr, tt, pp, swph=True)
    es = tdpack.mhraes(hr, tt, pp, outArray=es)

    Args:
        hr   : (numpy.ndarray, float32, F order) relative humidity (%)
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        swph : True  - consider water and ice phase
               False - consider water phase only (default)
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        dew point depressions (t-td) in K 
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> hr = np.array([0.1], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> es = tdpack.mhraes(hr, tt, pp)

    See also:
        mesahr
    """
    cni, cnk, cnn, es = _getOutArray(outArray, [hr, tt, pp])
    ciswph = _ct.c_int(1 if swph else 0)
    _tp.f_mhraes(es, hr, tt, pp, _ct.byref(ciswph), _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return es


def mesahu(es, tt, pp, swph=False, outArray=None):
    """
    Compute specific humidity from dew point depressions (t-td) in K 
    temperature and pressure

    hu = tdpack.mesahu(es, tt, pp)
    hu = tdpack.mesahu(es, tt, pp, swph=True)
    hu = tdpack.mesahu(es, tt, pp, outArray=hu)

    Args:
        es   : (numpy.ndarray, float32, F order) dew point depressions (t-td) in K
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        swph : True  - consider water and ice phase
               False - consider water phase only (default)
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        specific humidity [kg/kg]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> es = np.array([0.1], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hu = tdpack.mesahu(es, tt, pp)

    See also:
        mhuaes
    """
    cni, cnk, cnn, hu = _getOutArray(outArray, [es, tt, pp])
    ciswph = _ct.c_int(1 if swph else 0)
    _tp.f_mesahu(hu, es, tt, pp, _ct.byref(ciswph), _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return hu


def mesahr(es, tt, pp, swph=False, outArray=None):
    """
    Compute relative humidity from dew point depressions (t-td) in K 
    temperature and pressure

    hr = tdpack.mesahr(es, tt, pp)
    hr = tdpack.mesahr(es, tt, pp, swph=True)
    hr = tdpack.mesahr(es, tt, pp, outArray=hr)

    Args:
        es   : (numpy.ndarray, float32, F order) dew point depressions (t-td) in K 
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        swph : True  - consider water and ice phase
               False - consider water phase only (default)
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        relative humidity (%)
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> es = np.array([0.00001], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hr = tdpack.mesahr(es, tt, pp)

    See also:
        mhraes
    """
    cni, cnk, cnn, hr = _getOutArray(outArray, [es, tt, pp])
    ciswph = _ct.c_int(1 if swph else 0)
    _tp.f_mesahr(hr, es, tt, pp, _ct.byref(ciswph), _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return hr


def mfodla(tt, outArray=None):
    """
    Compute the derivative according to t of 'ln(ew)'
    (water phase considered only for all temperatures)

    de = tdpack.mfodla(tt)
    de = tdpack.mfodla(tt, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature in K
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        derivative on LN(EW)
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> de = tdpack.mfodla(tt)

    See also:
        
    """
    cni, cnk, cnn, de = _getOutArray(outArray, [tt])
    _tp.f_mfodla(de, tt, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return de


def mfodle(tt, outArray=None):
    """
    Compute the derivative of ln(ew) or ln(ei)
    w.r.t. tt for water or ice phase

    de = tdpack.mfodle(tt)
    de = tdpack.mfodle(tt, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature in K
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        derivative on ln(ew) or ln(ei)
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> de = tdpack.mfodle(tt)

    See also:
        
    """
    cni, cnk, cnn, de = _getOutArray(outArray, [tt])
    _tp.f_mfodle(de, tt, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return de


def mfotvt(tt, hu, outArray=None):
    """
    Compute virtual temperature tv
    from temperature tt and specific humidity hu

    tv = tdpack.mfotvt(tt, hu)
    tv = tdpack.mfotvt(tt, hu, outArray=tv)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature in K
        hu   : (numpy.ndarray, float32, F order) specific humidity in kg/kg
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        virtual temperature tv [K]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> tv = tdpack.mfotvt(tt, hu)

    See also:
       mfottv
       mfottvh
       mfotvht
    """
    cni, cnk, cnn, tv = _getOutArray(outArray, [tt, hu])
    _tp.f_mfotvt(tv, tt, hu, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return tv


def mfottv(tv, hu, outArray=None):
    """
    Compute temperature tt
    from virtual temperature tv and specific humidity hu

    tt = tdpack.mfottv(tv, hu)
    tt = tdpack.mfottv(tv, hu, outArray=tt)

    Args:
        tv   : (numpy.ndarray, float32, F order) virtual temperature in K
        hu   : (numpy.ndarray, float32, F order) specific humidity in kg/kg
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        temperature tt [K]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tv = np.array([273.15], dtype=np.float32, order='F')
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> tt = tdpack.mfottv(tv, hu)

    See also:
       mfotvt
       mfotvht
       mfottvh
    """
    cni, cnk, cnn, tt = _getOutArray(outArray, [tv, hu])
    _tp.f_mfottv(tt, tv, hu, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return tt


def mfotvht(tt, hu, qh, outArray=None):
    """
    Compute virtual temperature tv
    from temperature tt and specific humidity hu
    and specific mass of hydrometeors qh.
    Note - The virtual temperature here is the one that accounts
    for the vapor and the hydrometeors.

    tv = tdpack.mfotvht(tt, hu, qh)
    tv = tdpack.mfotvht(tt, hu, qh, outArray=tv)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature in K
        hu   : (numpy.ndarray, float32, F order) specific humidity in kg/kg
        qh   : (numpy.ndarray, float32, F order) specific mass of hydrometeors in kg/kg
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        virtual temperature tv [K]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> qh = np.array([0.00001], dtype=np.float32, order='F')
    >>> tv = tdpack.mfotvht(tt, hu, qh)

    See also:
       mfottv
       mfottvh
       mfotvt
    """
    cni, cnk, cnn, tv = _getOutArray(outArray, [tt, hu, qh])
    _tp.f_mfotvht(tv, tt, hu, qh, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return tv


def mfottvh(tv, hu, qh, outArray=None):
    """
    Compute temperature tt
    from virtual temperature tv and specific humidity hu
    and specific mass of hydrometeors qh.
    Note - The virtual temperature here is the one that accounts
    for the vapor and the hydrometeors.

    tt = tdpack.mfottvh(tv, hu, qh)
    tt = tdpack.mfottvh(tv, hu, qh, outArray=tt)

    Args:
        tv   : (numpy.ndarray, float32, F order) virtual temperature in K
        hu   : (numpy.ndarray, float32, F order) specific humidity in kg/kg
        qh   : (numpy.ndarray, float32, F order) specific mass of hydrometeors in kg/kg
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        temperature tt [K]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tv = np.array([273.15], dtype=np.float32, order='F')
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> qh = np.array([0.00001], dtype=np.float32, order='F')
    >>> tt = tdpack.mfottvh(tv, hu, qh)

    See also:
       mfotvt
       mfotvht
       mfottv
    """
    cni, cnk, cnn, tt = _getOutArray(outArray, [tv, hu, qh])
    _tp.f_mfottvh(tt, tv, hu, qh, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return tt


def mfodqa(tt, pp, outArray=None):
    """
    Compute the derivative of QSAT(saturation specific humidity)
    according to T (water phase considered only for all temperatures)

    dq = tdpack.mfodqa(tt, pp)
    dq = tdpack.mfodqa(tt, pp, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        derivative of QSAT (saturation specific humidity)
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> dq = tdpack.mfodqa(tt, pp)

    See also:
        mfodqs
    """
    cni, cnk, cnn, dq = _getOutArray(outArray, [tt, pp])
    _tp.f_mfodqa(dq, tt, pp, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return dq


def mfodqs(tt, pp, outArray=None):
    """
    Compute the derivative of QSAT(saturation specific humidity)
    according to T (water and ice phase considered only for all temperatures)

    dq = tdpack.mfodqs(tt, pp)
    dq = tdpack.mfodqs(tt, pp, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        derivative of QSAT (saturation specific humidity)
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> dq = tdpack.mfodqs(tt, pp)

    See also:
        mfodqa
    """
    cni, cnk, cnn, dq = _getOutArray(outArray, [tt, pp])
    _tp.f_mfodqs(dq, tt, pp, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return dq


def mfoqsa(tt, pp, outArray=None):
    """
    Compute specific humidity at saturation (water only) in kg/kg

    hu = tdpack.mfoqsa(tt, pp)
    hu = tdpack.mfoqsa(tt, pp, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        specific humidity at saturation (water only)
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hu = tdpack.mfoqsa(tt, pp)

    See also:
        mfoqst
    """
    cni, cnk, cnn, hu = _getOutArray(outArray, [tt, pp])
    _tp.f_mfoqsa(hu, tt, pp, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return hu


def mfoqst(tt, pp, outArray=None):
    """
    Compute specific humidity at saturation in kg/kg

    hu = tdpack.mfoqst(tt, pp)
    hu = tdpack.mfoqst(tt, pp, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        specific humidity at saturation
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hu = tdpack.mfoqst(tt, pp)

    See also:
        mfoqsa
    """
    cni, cnk, cnn, hu = _getOutArray(outArray, [tt, pp])
    _tp.f_mfoqst(hu, tt, pp, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return hu


def mfoqfe(ee, pp, outArray=None):
    """
    Compute specific humidity from vapour pressure and pressure

    hu = tdpack.mfoqfe(ee, pp)
    hu = tdpack.mfoqfe(ee, pp, outArray=de)

    Args:
        ee   : (numpy.ndarray, float32, F order) vapour pressure in Pa 
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        specific humidity [kg/kg]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> ee = np.array([1.], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hu = tdpack.mfoqfe(ee, pp)

    See also:
        mfoefq
    """
    cni, cnk, cnn, hu = _getOutArray(outArray, [ee, pp])
    _tp.f_mfoqfe(hu, ee, pp, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return hu


def mfoefq(hu, pp, outArray=None):
    """
    Compute vapour pressure from specific humidity and pressure

    ee = tdpack.mfoefq(hu, pp)
    ee = tdpack.mfoefq(hu, pp, outArray=de)

    Args:
        hu   : (numpy.ndarray, float32, F order) specific humidity [kg/kg]
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        vapour pressure [Pa]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> ee = tdpack.mfoefq(hu, pp)

    See also:
        mfoqfe
    """
    cni, cnk, cnn, ee = _getOutArray(outArray, [hu, pp])
    _tp.f_mfoefq(ee, hu, pp, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return ee


def mfoeic(tt, outArray=None):
    """
    Compute saturated vapour pressure (ice only) from temperature

    ei = tdpack.mfoeic(tt)
    ei = tdpack.mfoeic(tt, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature [K]
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        saturated vapour pressure (ice only) [Pa]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> ei = tdpack.mfoeic(tt)

    See also:
        mfoew
        mfoewa
    """
    cni, cnk, cnn, ei = _getOutArray(outArray, [tt])
    _tp.f_mfoeic(ei, tt, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return ei


def mfoew(tt, outArray=None):
    """
    Compute saturated vapour pressure (water and ice) from temperature

    ew = tdpack.mfoew(tt)
    ew = tdpack.mfoew(tt, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature [K]
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        saturated vapour pressure (water and ice) [Pa]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> ew = tdpack.mfoew(tt)

    See also:
        mfoeic
        mfoewa
    """
    cni, cnk, cnn, ew = _getOutArray(outArray, [tt])
    _tp.f_mfoew(ew, tt, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return ew


def mfoewa(tt, outArray=None):
    """
    Compute saturated vapour pressure (water and ice) from temperature

    ew = tdpack.mfoewa(tt)
    ew = tdpack.mfoewa(tt, outArray=de)

    Args:
        tt   : (numpy.ndarray, float32, F order) temperature [K]
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        saturated vapour pressure (water and ice) [Pa]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> ew = tdpack.mfoewa(tt)

    See also:
        mfoeic
        mfoew
    """
    cni, cnk, cnn, ew = _getOutArray(outArray, [tt])
    _tp.f_mfoewa(ew, tt, _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return ew


def mfohr(hu, tt, pp, satuco=False, outArray=None):
    """
    Compute relative humidity from specific humidity,
    temperature and pressure

    hr = tdpack.mfohr(hu, tt, pp)
    hr = tdpack.mfohr(hu, tt, pp, satuco=True)
    hr = tdpack.mfohr(hu, tt, pp, outArray=hr)

    Args:
        hu     : (numpy.ndarray, float32, F order) specific humidity in kg/kg
        tt     : (numpy.ndarray, float32, F order) temperature in K
        pp     : (numpy.ndarray, float32, F order) pressure in Pa
        satuco : True  - consider water and ice phase
                 False - consider water phase only (default)
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        relative humidity (%)
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hr = tdpack.mfohr(hu, tt, pp)

    See also:
        mhuahr
        mhrahu
    """
    cni, cnk, cnn, hr = _getOutArray(outArray, [hu, tt, pp])
    cisatuco = _ct.c_int(1 if satuco else 0)
    _tp.f_mfohr(hr, hu, tt, pp, _ct.byref(cisatuco), _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return hr


## #TODO: recheck this function, code seams to indicate that PN is needed and HU is I/O
## def modhui(tt, swph=False, outArray=None):
##     """
##     Compute relative humidity from specific humidity,
##     temperature and pressure

##     hu = tdpack.modhui(hu, tt)
##     hu = tdpack.modhui(hu, tt, swph=True)
##     hu = tdpack.modhui(hu, tt, outArray=hu)

##     Args:
##         hu     : (numpy.ndarray, float32, F order) specific humidity in kg/kg
##         tt   : (numpy.ndarray, float32, F order) temperature in K
##         swph : True  - consider water and ice phase
##                False - consider water phase only (default)
##         outArray : (optional) output array (default: new np.array)
##     Returns:
##         numpy.ndarray (F order, same type and shape as input)
##         specific humidity [kg/kg]
##     Raises:
##         TypeError   on wrong input arg types
##         ValueError  on invalid input arg value
##         TDPackError on any other error
##     Notes:
##         New function in version 2.2.0-a20

##     Examples:
##     >>> import rpnpy.tdpack.all as tdpack
##     >>> import numpy  as np
##     >>> tt = np.array([273.15], dtype=np.float32, order='F')
##     >>> hu = tdpack.modhui(tt)

##     See also:
##         mhuahr
##     """
##     cni, cnk, cnn, hu = _getOutArray(outArray, [tt])
##     ciswph = _ct.c_int(1 if swph else 0)
##     _tp.f_modhui(hu, tt, _ct.byref(ciswph), _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
##     return hu


def mthtaw(hu, tt, pp, swph=False, swth=False, ti=None, outArray=None):
    """
    Compute TW or THETAW (according to the value SWTH)
    from specific humidity, temperature and pressure

    tw = tdpack.mthtaw(hu, tt, pp)
    tw = tdpack.mthtaw(hu, tt, pp, swph=True)
    tw = tdpack.mthtaw(hu, tt, pp, swph=True, swth=True)
    tw = tdpack.mthtaw(hu, tt, pp, swph=True, swth=True, ti=270.)
    tw = tdpack.mthtaw(hu, tt, pp, outArray=hr)

    Args:
        hu   : (numpy.ndarray, float32, F order) specific humidity in kg/kg
        tt   : (numpy.ndarray, float32, F order) temperature in K
        pp   : (numpy.ndarray, float32, F order) pressure in Pa
        swph : True  - consider water and ice phase
               False - consider water phase only (default)
        swth : True  - Compute ThetaW
               False - Compute TW (default)
        ti   : temperature in K at which we start calculating
               latent heat of sublimation
               if swph=False, ti is n/a
               ti must be <= TRPL
        outArray : (optional) output array (default: new np.array)
    Returns:
        numpy.ndarray (F order, same type and shape as input)
        TW or ThetaW (according to the value swth) [K]
    Raises:
        TypeError   on wrong input arg types
        ValueError  on invalid input arg value
        TDPackError on any other error
    Notes:
        New function in version 2.2.0-a20
        call tdpack's mthtaw3 function if not "ti" is provided
        call tdpack's mthtaw4 function if "ti" is provided

    Examples:
    >>> import rpnpy.tdpack.all as tdpack
    >>> import numpy  as np
    >>> hu = np.array([0.00001], dtype=np.float32, order='F')
    >>> tt = np.array([273.15], dtype=np.float32, order='F')
    >>> pp = np.array([80000.], dtype=np.float32, order='F')
    >>> hr = tdpack.mthtaw(hu, tt, pp)
    >>> hr = tdpack.mthtaw(hu, tt, pp, swph=True, swth=True, ti=270.)

    See also:
        
    """
    cni, cnk, cnn, tw = _getOutArray(outArray, [hu, tt, pp])
    ciswph = _ct.c_int(1 if swph else 0)
    ciswth = _ct.c_int(1 if swth else 0)
    if ti is None:
        _tp.f_mthtaw3(tw, hu, tt, pp, _ct.byref(ciswph), _ct.byref(ciswth),
                      _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    else:
        cti = _ct.c_float(ti)
        _tp.f_mthtaw4(tw, hu, tt, pp, _ct.byref(ciswph), _ct.byref(ciswth),
                      _ct.byref(cti),
                      _ct.byref(cni), _ct.byref(cnk), _ct.byref(cnn))
    return tw



if __name__ == "__main__":
    import doctest
    doctest.testmod()

# -*- Mode: C; tab-width: 4; indent-tabs-mode: nil -*-
# vim: set expandtab ts=4 sw=4:
# kate: space-indent on; indent-mode cstyle; indent-width 4; mixedindent off;
