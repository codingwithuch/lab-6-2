# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:18:51 2023

@author: noopk
"""
import numpy as np
from DataAnaysisTools import statisticalUncertanity, totalUncertainty,reportMeaurement,relativeUncertainty,discrepancy,combinedMeasurement

set_1 = reportMeaurement([72.2,77.6,82.4,86.3,88.9], 0.3)
set_2 = reportMeaurement([80.1,81.45,81.5,81.34,82.01], 0.05)

print("")

print("data set 1 measurement is in the range of [ " + str(set_1[0]) + " , " + str(set_1[1]) + " ] in cm ")
print("data set 2 measurement is in the range of [ " + str(set_2[0]) + " , " + str(set_2[1]) + " ] in cm")

unc_1 = relativeUncertainty([72.2,77.6,82.4,86.3,88.9],0.3)
unc_2 = relativeUncertainty([80.1,81.45,81.5,81.43,82.01],0.05)

print("uncertainty for the first set is " + str(round(unc_1,3)) + " %")
print("uncertainty for the 2nd set is " + str(round(unc_2,3)) + " %")

agree_maybe = discrepancy(np.mean([72.2,77.6,82.4,86.3,88.9]), unc_1, np.mean([80.1,81.45,81.5,81.43,82.01]), unc_2)
print(agree_maybe)


combined = combinedMeasurement([np.mean([72.2,77.6,82.4,86.3,88.9]),np.mean([80.1,81.45,81.5,81.43,82.01])], [unc_1,unc_2])
print("the combined result is " + str(combined))
print("1st num in the avg, 2nd number is the error")





