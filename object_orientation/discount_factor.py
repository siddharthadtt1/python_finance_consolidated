# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:43:27 2017

@author: sd835979
"""

def discount_factor(r, t):
    """
        Function to calculate a discount factor.
        
        Parameters
        ===========
        r : float
            positive, constant short rate
        t : float , array of floats
            future date(s), in fraction of years;
            e.g. 0.5 means half a year from now
            
        Returns
        ========
        df : float
            discount factor 
    
    """
    import numpy as np
    
    df = np.exp(-r * t)
    # use of Numpy universal function for vectorization
    return df

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 5)
rate_arr = [0.01, 0.05, 0.1]

for r in rate_arr:
    plt.plot(t, discount_factor(r, t), label='r=%3.2f' % r , lw=2)

plt.xlabel('years')
plt.ylabel('discount factor')
plt.grid(True)
plt.legend(loc=0)
        
    