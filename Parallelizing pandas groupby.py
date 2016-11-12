# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:43:42 2016

@author: jonathan
"""

import sys
import pandas as pd
import numpy as np
from numpy import random

"""
def take_input():
    try: 
        return float(raw_input().strip())
    except ValueError:
        return None


n = take_input()
"""


DF = pd.DataFrame(data = random.randint(low = 1, high = 100, size = (10**7, 4)), columns = ['a', 'b', 'c', 'd'])    


def some_function(df):
    minimum = df['a'].min() * random.rand()
    results = (df['b'] - minimum).mean()
    return pd.Series(data = results)
    
    
#some_function(DF) ## works
 
myresults = DF.groupby(by = ['c', 'd']).apply(some_function)


grouped = DF.groupby(by = ['c', 'd'], sort=False)

for name, group in grouped:
    print name
    print group.head()
    print "** results from some function **"
    s = some_function(group)
    print s
    multiindex = pd.MultiIndex.from_tuples([name], names = ['c', 'd'])
    print multiindex
    print " Series with MultiIndex "
    s.index = multiindex
    print s
    break





### parallel version ###

def mask_some_function(myTuple):
    name = myTuple[0]
    df = myTuple[1]
    s = some_function(df)
    multiindex = pd.MultiIndex.from_tuples([name], names = ['c', 'd'])
    s.index = multiindex
    return s


from multiprocessing import Pool, cpu_count

def parallel_groupby(fun, groups):
    p = Pool(processes=cpu_count())
    results = p.map(fun, iterable=[(name,group) for name, group in groups])
    return pd.concat(results)
    
