#!/usr/bin/nv python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# Filename: fAux.py
# --------------------------------------------------------------------
"""
   Funciones auxiliares a svm.py

"""

import numpy as np

def backshift(day,x):
    assert day > 0,'Invalid day'
    shift = np.zeros((np.shape(x)))
    shift[day:] = x[:-day]
    shift[shift==0] = np.nan
    return shift

def calculateReturns(prices, lag):
    prevPrices = backshift(lag, prices)
    rlag = (prices - prevPrices) / prevPrices
    return rlag

def fwdshift(day,x):
    assert day > 0,'Invalid day'
    shift = np.zeros((np.shape(x)))
    shift[:-day] = x[day:]
    shift[shift==0] = np.nan
    return shift

def calculateMaxDD(cumret):
    highwatermark = np.zeros(len(cumret))
    drawdown      = np.zeros(len(cumret))
    drawdownduration = np.zeros(len(cumret))
    for t in range(1, len(cumret)):
        highwatermark[t] = np.max([highwatermark[t-1], cumret[t]])
        drawdown[t] = (1+cumret[t]) / (1 + highwatermark[t]) - 1
        if (drawdown[t]==0):
            drawdownduration[t] = 0
        else:
            drawdownduration[t] = drawdownduration[t-1] + 1
    return np.min(drawdown), np.max(drawdownduration)


def main():
    pass

if (__name__ == '__main__'):
    main()
