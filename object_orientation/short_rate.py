# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:03:07 2017

@author: sd835979
"""

class short_rate(object):
    """
        Class to model a constant short rate object.
        
    Parameters
    ==========
    name : string
            name of the object
    rate : float
            positive, constant short rate
    
    Methods
    =======
    get_discount_factors :
        returns discount factor for given list/array
        of dates/times (as year fractions)
    
    """
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
    
    def get_discount_factors(self, time_list):
        " time_list : list/array-like "
        import numpy as np
        time_list = np.array(time_list)
        return np.exp(-self.rate * time_list)
    