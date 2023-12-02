# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 18:12:59 2023

@author: noopk
"""
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from DataAnaysisTools import statisticalUncertanity, totalUncertainty,reportMeaurement,relativeUncertainty,discrepancy,combinedMeasurement,lineFit,relativeError,lineFitWt,fitQuality



resistance, resistance_unc, current, current_unc = np.loadtxt("voltage4.txt",delimiter=",", unpack = True, skiprows = 0)

resistance_unc.sort()
current_unc.sort()
current.sort()
resistance.sort()


#getting voltage
voltage = [i * j for i,j in zip(current,resistance)]
voltage_unc = [((i*j)**2 + (k * l)**2)**(1/2) for i,j,k,l in zip(resistance,current_unc,current,resistance_unc)]



#plotting data
plt.plot(resistance, voltage, label = "volt v resitance")
plt.errorbar(resistance, voltage, label = "data" , yerr = voltage_unc, xerr = resistance_unc, fmt = 'oC1', ecolor = "black")


#linewj
mw = lineFitWt(resistance, voltage, voltage_unc)[0]
bw = lineFitWt(resistance, voltage, voltage_unc)[1]
d = np.linspace(min(resistance),max(resistance),25)

plt.plot(d, mw * d + bw, color = "red", label = "weighted avg")

plt.legend(loc = "best")

print(fitQuality(resistance, voltage, voltage_unc))

print("the fit quiality is supper far away from one, so I say that it does not obey the ohms laws")