# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 01:07:29 2021

@author: NPass
"""

import numpy as np
import pandas as pd

lista = np.random.rand(9)

def calculate(input):

  if len(input)!=9:
      raise ValueError('List must contain nine numbers.')
  else:
      
    input = np.array(input)

    mtx = np.reshape(input,(3,3))

    mean = [np.mean(mtx , axis=0).tolist() , np.mean(mtx , axis=1).tolist() , np.mean(mtx)]
    var = [np.var(mtx, axis = 0).tolist() , np.var(mtx , axis =1).tolist() , np.var(mtx)]
    std_dev = [np.std(mtx , axis = 0).tolist() , np.std(mtx , axis=1).tolist() , np.std(mtx)]
    max_mtx = [np.max(mtx , axis = 0).tolist() , np.max(mtx , axis=1).tolist() , np.max(mtx)]
    min_mtx = [np.min(mtx , axis = 0).tolist() , np.min(mtx , axis=1).tolist() , np.min(mtx)]
    sum_mtx = [np.sum(mtx , axis = 0).tolist() , np.sum(mtx , axis=1).tolist() , np.sum(mtx)]

    calculations = {'mean' : mean,
              'variance' : var,
              'standard deviation' : std_dev,
              'max' : max_mtx,    
              'min' : min_mtx,
              'sum' : sum_mtx }
    
  return calculations
  

calculations = calculate(lista)
