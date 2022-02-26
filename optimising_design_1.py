#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:58:42 2022

@author: aliyah
"""

import numpy as np
import matplotlib.pyplot as plt

f1 = 11.671 #LA1540-B
f2 = 400.654 #LB1862-B
fbb = 41.856 #Blackbox
f = [f1,f2,fbb]



S1 = 21.881
S3 = 16.922
S4 = 45.246

#%%
S2 = np.arange(313.9,314.75, 0.05)
w = [2.82181E-03	,2.72098E-03	,2.62982E-03	,2.54936E-03	,2.48065E-03	,2.42469E-03,2.38237E-03	,2.35444E-03	,2.34140E-03	,2.34350E-03	,2.36070E-03,2.39269E-03	,2.43887E-03	,2.49846E-03	,2.57053E-03	,2.65406E-03, 2.74800E-03,2.85133E-03	   	                  	]
w0 = [2.34386E-03,2.34345E-03,2.34303E-03,2.34262E-03,2.34220E-03,2.34179E-03,2.34138E-03,2.34096E-03,2.34055E-03,2.34013E-03,2.33972E-03,2.33931E-03,2.33889E-03,2.33848E-03,2.33807E-03,2.33765E-03 ,2.33724E-03,2.33683E-03	            ]
Ray = [3.13799E-02,3.13688E-02,3.13577E-02,3.13466E-02,3.13355E-02,3.13244E-02,3.13133E-02,3.13023E-02,3.12912E-02, 3.12801E-02,3.12691E-02,3.12580E-02,3.12470E-02,3.12359E-02,3.12249E-02,3.12139E-02 , 3.12028E-02,3.11918E-02      ]
z = []

for i in S2:
    z_ = S1+S3+S4+i
    z.append(z_)


plt.plot(S2,w, 'x', label = 'beam size in ion plane')
plt.plot(S2,w0,'.', label = 'waist')
plt.legend()
plt.xlabel('lens separation')







cf =  np.polyfit(S2,w,2)
y = np.poly1d(cf)
plt.plot(S2,y(S2))

c =  np.polyfit(S2,w0,1)
yf = np.poly1d(c)
plt.plot(S2,yf(S2))

plt.figure(2)
plt.plot(S2,z,'x')
plt.ylabel('Z0')
plt.xlabel('lens separation')