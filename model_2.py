#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:41:12 2022

@author: aliyah
"""

import numpy as np
import math
import matplotlib.pyplot as plt

Lambda= 0.000729
pi = np.pi


def Free_s(d):
    
    a = np.array([[1,d],[0,1]])
    
    return a

def lens(n1,n2,s,R1,R2):
    '''
    Thick lens matrix

    Parameters
    ----------
    n1 : float
        Refractive index outside of the lens
    n2 : float
        Refractive index of the lens itself (inside the lens)
    s :  float
        Center thickness of lens
    R1 : float
        Radius of curvature of First surface.
    R2 : float
        Radius of curvature of Second surface.

    Returns
    -------
    Lens matrix 

    '''
    a = np.array([[1,0],[(n1-n2)/(R1*n2) , n1/n2]])  # first surface
    
    b = np.array([[1,s],[0,1]])  # in the lens
    
    c = np.array([[1,0],[(n2-n1)/(R2*n1) , n2/n1]]) # second surface
    
    #print(a,b,c)
    
    return np.matmul(np.matmul(c,b),a)


def waist_trace(matrix,q):
    
    Q = ( matrix[1][0] * q + matrix[1][1] ) / ( matrix[0][0] * q + matrix[0][1] )
    
    w = np.sqrt( -Lambda / pi / Q.imag)
    #print(matrix[1][0])
    
    return w , Q**-1

def ray_trace(source, abcd):
    
    r = [source]
    
    for i in range(len(abcd)):
        
        R = np.matmul(abcd[-1],r[-1])
        abcd.pop(-1)
        r.append(R)
    
    return r
        
            
        
            
        
#%%
### trace q

a = Free_s(10)
b = Free_s(50)
Lens1 = lens(1, 1.515, 2.5, 5.2, math.inf)
f = Free_s(20)
g = Free_s(104.388)
Lens2 = lens(1, 1.515, 9.47, 101.4, -101.4)
k = Free_s(20)

S = [10,50,2.5,20,104.388,9.47,20] #list of separations between surfaces
s_ = [] #list of cumulative sum of separations
for i in range(0,len(S)):
    if i == 0:
        s_.append(S[i])
    else:
        s_.append(S[i]+s_[i-1])


#%%

Sur = [0,1,2,3,4,5,6,7]
Ww =  [5.00000E-02,6.82191E-02,2.82911E-01, 2.44564E-01,2.27660E-01,2.69004E+00,2.75264E+00,2.67435E+00]



#%%
w0 = [0.05]
w = [w0[0]]
Z = []

q0 = 1j * pi * w[0]**2 / Lambda
q = [q0]



abcd = [a,b,Lens1,f,g,Lens2,k]

for i in range(len(abcd)) :
    
    W,Q = waist_trace(abcd[i],q[-1])
    z = s_[i]
    w0_ = np.sqrt(Q.imag*Lambda/np.pi)
    #print([i,W])
    w.append(W)
    q.append(Q)
    w0.append(w0_)
    Z.append(z)

number = np.linspace(0,7,8)

plt.figure(1)
plt.plot(number,w,'x',label='simulation')
plt.plot(Sur,Ww,'o',label='zemax')
plt.xlabel('surface number')
plt.ylabel('beam size at surface')
plt.legend()

#%%
plt.figure(2)
plt.title('Waist at each surface')
plt.plot(number, w0, label = 'simulation')

#%%
r0 = np.array([[1],[0]])