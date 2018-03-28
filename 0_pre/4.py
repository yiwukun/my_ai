# -*- coding:UTF-8 -*-
import numpy as np

#定义sigmoid函数
"""
1.tanh函数
2.逻辑函数
"""
def tanh(x):
# return np.tanh(x)
    np.tanh(x)

# 求导
def tanh_derv(x):
    return 1.0 - np.tanh(x)*np.tanh(x)

def logistic(x):
    return 1 / (1+np.exp(-x))