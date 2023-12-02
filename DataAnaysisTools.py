# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:46:46 2023

@author: noopk
"""

import numpy as np


def statisticalUncertanity(xdata):
    N = len(xdata) 
    x_mean = np.mean(xdata) 
    NN = N * (N-1)
    NNN = (NN)**(-1)  # 1 / (N*(N-1))
    u = [] #empty list for storing data later
    for i in xdata:
        u.append(((i- x_mean) ** 2))
    u_tot = sum(u)  #(x_avg - x_1)^2 summed up
    first = u_tot * NNN
    second = first ** (1/2)  #final result 
    return second
   

def totalUncertainty(xdata,typeBUnc = 0):
    third = typeBUnc**2 #squaring the data for later (type b)
    fourth = (statisticalUncertanity(xdata))**2 #type a uncerticnity squared
    fith = 2 * np.sqrt(third + fourth) #finshes the calcs
    print("this value" + str(fith))
    return fith



def reportMeaurement(xdata,typeBUnc = 0):
    avg_x = np.mean(xdata)
    small_x = avg_x - totalUncertainty(xdata,typeBUnc) #min
    large_x = avg_x + totalUncertainty(xdata,typeBUnc) #max
    return (small_x, large_x, totalUncertainty(xdata,typeBUnc))

def relativeUncertainty(xdata,typeBUnc = 0):
    avg_x = np.mean(xdata)
    x_best_pos = (avg_x)**2
    x_best_pos_2 = (x_best_pos) ** (1/2)  # (x^2) ^(1/2) = abs(x)
    x_best_pos_inv = (x_best_pos_2) ** (-1)
    rel_unc = x_best_pos_inv * totalUncertainty(xdata, typeBUnc)
    return rel_unc * 100

def discrepancy(xbest1,dx1,xbest2,dx2):
    #sixth = (xbest1-xbest2)**2 
    #seveth = (sixth) ** (1/2) #abs trick for avg
    seveth = np.absolute(xbest1-xbest2)
    #eight = (dx1+dx2)**2 
    #nine = (eight) ** (1/2) #abs trick for error
    nine = np.absolute(dx1 + dx2)
    ten = seveth < nine #agree?
    return (seveth,nine,ten)

def combinedMeasurement(xresults, dxresults):
    w_j = [i**(-2) for i in dxresults]  # taking the inverse squared
    w_j_sum = sum(w_j)
    w_j_sum_inv = w_j_sum ** (-1)
    delta_x_com = w_j_sum_inv ** 0.5  # find the w_j sum and take the inverse square root
    helper = [i * j for i, j in zip(xresults, w_j)]  # x * w_j
    helper_2 = sum(helper)  # x * w_j sum
    x_best_com = helper_2 * w_j_sum_inv
    return x_best_com, delta_x_com


def lineFit(x,y):
    N = len(x)
    N_inv = N ** (-1)
    E_x = sum(x) * N_inv
    E_y = sum(y) * N_inv
    xtimesx = [i * j for i,j in zip(x,x)] #setup for below
    E_xx = sum(xtimesx) * N_inv
    xtimesy = [i * j for i,j in zip(x,y)] #setup for below
    E_xy = sum(xtimesy) * N_inv
    #just setting up some varibles for later use
    m_num = E_xy - E_x * E_y
    b_num = E_xx * E_y - E_x * E_xy
    mn_dem = E_xx - E_x * E_x
    mn_dem2 = mn_dem ** (-1)
    m = m_num * mn_dem2
    b = b_num * mn_dem2
    return m,b

def relativeError(xmeasured,xaccepted):
    num = xmeasured - xaccepted
    dem = xaccepted ** (-1)
    error1 = num * dem
    error2 = np.absolute(error1)
    return error2

def lineFitWt (x,y,dy):
    dyy = [i ** (-2) for i in dy]
    w = sum(dyy)
    #converted dy to the 1/y^2 thing
    wxy = [i*j*k for i,j,k in zip(x,y,dyy)]
    Swxy = sum(wxy)
    #first made everything into a single list then we summed it up
    wx = [i*k for i,k in zip(x,dyy)]
    Swx = sum(wx)
    #repeat
    wy = [i*j for i,j in zip(y,dyy)]
    Swy = sum(wy)
    #repeat
    wxx = [i*j*k for i,j,k in zip(dyy,x,x)]
    Swxx = sum(wxx)
    #repeat
    #these are all the values we need for this
    
    
    #finding m
    m_num = w * Swxy - Swx * Swy
    m_dem = w * Swxx - Swx * Swx
    m_dem2 = m_dem ** (-1)
    #find the num and dem seperately then multiply it out
    m_weight = m_num * m_dem2
    
    
    
    #finding b
    b_num = Swxx * Swy - Swx* Swxy
    b_dem = w * Swxx - Swx * Swx
    b_dem2 = b_dem ** (-1)
    #Simliar
    b_weight = b_num * b_dem2
    
    #deltamw
    dm_num = w**(1/2)
    dm_dem = (w*Swxx - Swx*Swx) ** (-1/2)
    dm = dm_num * dm_dem
    
    #deltabw
    db_num = (Swxx) ** (1/2)
    db_dem = (w * Swxx - Swx*Swx) ** (-1/2)
    db = db_num * db_dem
    
    
    return m_weight,b_weight, dm, db


def fitQuality(x,y,dy):
    m = lineFitWt(x,y,dy)[0]
    b = lineFitWt(x,y,dy)[1]
    N = len(x)
    N2 = (N-2) ** (-1)
    #setting up some varibles
    
    
    mx = [m * i for i in x]
    num_q = [(i-j - b) for i,j in zip(y,mx)]
    dem_q = [i ** (-1) for i in dy]
    ele_of_q = [(i * j) * (i * j) for i,j in zip(num_q,dem_q)]
    #setting up the interior of the summation
    q_add = sum(ele_of_q)
    #summing
    q = N2 * q_add
    return(q)





    
    
    
    

    
    
    
    
    
    
    
    
    

    
    


    
    




    
        
    

    
    



    








        
    