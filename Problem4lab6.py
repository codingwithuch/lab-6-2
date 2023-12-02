# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:54:29 2023

@author: noopk
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DataAnaysisTools import statisticalUncertanity, totalUncertainty,reportMeaurement,relativeUncertainty,discrepancy,combinedMeasurement,lineFit,relativeError,lineFitWt,fitQuality

time, velocity, uncertainty = np.loadtxt("fallingmass.txt",delimiter=",", unpack = True)

x = time
y = velocity
dy = uncertainty

m_uw = lineFit(x, y)[0]
b_uw = lineFit(x, y)[1]
#unweighted data

m_w = lineFitWt(x, y, dy)[0]
b_w = lineFitWt(x, y, dy)[1]
#weighted data

d = np.linspace(min(x),max(x),25)
#domian of what i am graphing

plt.plot(d, m_uw * d + b_uw, label = "unweighted")
plt.errorbar(x,y, fmt = 'oC1' , label = "data", yerr = dy, ecolor = 'black', xerr = 0 )
plt.plot(d, m_w * d + b_w,  label = "weighted")
plt.legend(loc = 'best')

print("unweighted slope is " + str(m_uw) + " and the intercept is " + str(b_uw))
print("weighted slope is " + str(m_w) + " and the intercept is " + str(b_w))

plt.savefig("Problem 3 fig")

print("Our slope will be steeper with the weighted averages. This is because our data does not fit a line well,you tend to fall faster as time goes on, weighted averages will incoperate this into the data more strongly than unweighted averages")
print("Our slope uncertinaitny range is [" + str(m_w - lineFitWt(x, y, dy)[2]) + ","  + str( m_w + lineFitWt(x, y, dy)[2]) + "]")
print("Our intercept uncertinaitny range is [" + str(m_w - lineFitWt(x, y, dy)[3]) + ","  + str( m_w + lineFitWt(x, y, dy)[3]) + "]")




