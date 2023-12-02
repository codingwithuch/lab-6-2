# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:19:35 2023

@author: noopk
"""
import matplotlib.pyplot as plt
import numpy as np
from DataAnaysisTools import statisticalUncertanity, totalUncertainty,reportMeaurement,relativeUncertainty,discrepancy,combinedMeasurement,lineFit,relativeError,lineFitWt,fitQuality

x_vals = [5.4874 * 10**(14), 6.931 * 10**(14), 7.4307 * 10**(14), 8.2193 * 10**(14), 9.6074 * 10**(14), 1.184 * 10**(15)]
y_vals = [0.5309,1.0842,1.2734,1.6598,2.19856,3.10891]
plt.plot(x_vals,y_vals, marker = "o")
# above is a manual plot


m = lineFit(x_vals,y_vals)[0]
b = lineFit(x_vals,y_vals)[1]
#lineFitWt(x_vals,y_vals,np.ones(len(y_vals)))
#commented line above shows that my function is valid
print("fit q" + str(fitQuality(x_vals, y_vals, np.ones(len(y_vals)))))

x = np.linspace(min(x_vals),max(x_vals),25)
plt.plot(x, m*x+b)
#line of best fit is above

e = 1.602176634 * (10 ** (-19))

h_guess = m * e

print(h_guess)

h_true = 6.62607015 * 10 ** (-34)

print("my error for my h value is....")
print(round(relativeError(h_guess, h_true) * 100,2))
print("%")












