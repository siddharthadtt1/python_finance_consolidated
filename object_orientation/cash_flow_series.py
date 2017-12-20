# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:29:17 2017

@author: sd835979
"""

class cash_flow_series(object):
    """
        Class to model a cash flow series
        
        Attributes
        ==========
        name : string
            name of the object
        cash_flows : list/array-like
            list of (positive) year fractions
        time_list : list/array-like
            corresponding list of cash flow values
        short_rate : instance of short_rate class 
            short rate object used for discounting
            
        Methods
        =======
        present_value_list :
            returns an array with present values
        net_present_value :
            returns NPV for cash flow series
            
    """
    import numpy as np
    
    def __init__(self, name, cash_flows, time_list, short_rate):
        self.name = name
        self.cash_flows = cash_flows
        self.time_list = time_list
        self.short_rate = short_rate
    
    def present_value_list(self):
        df = self.short_rate.get_discount_factors(self.time_list)
        return np.array(self.cash_flows) * df
        
    def net_present_value(self):
        return np.sum(self.present_value_list())
    
class cfs_sensitivity(cash_flow_series):
    """
        Class to net model cash flow for a range of short rates
        
        Attributes
        ===========
        short_rates : list/array-like
            corresponding list of short_rates
        
        Methods
        =======
        npv_sensitivity :
            returns an array of npv for corresponding range of short rates
        
    """
    import numpy as np
    def npv_sensitivity(self, short_rates):
        self.npvs = []
        self.short_rates = short_rates
        for rate in short_rates:
            self.short_rate.rate = rate
            self.npvs.append(self.net_present_value())
        self.npvs = np.array(self.npvs)
        return self.npvs
            
    
    def display_chart(self, short_rates):
        import matplotlib.pyplot as plt
        self.npv_sensitivity(short_rates)
        plt.plot(self.short_rates, self.npvs, 'b')
        plt.plot(self.short_rates, self.npvs, 'ro')
        plt.plot((0, max(self.short_rates)), (0, 0), 'r', lw=2)
        plt.grid(True)
        plt.xlabel(' short rate ')
        plt.ylabel(' net present values ')
                
        