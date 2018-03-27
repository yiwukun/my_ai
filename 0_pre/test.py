# -*- coding: utf-8 -*-
"""
YANG
这是一个安装包测试代码 

"""

import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

#矩阵运算库
import numpy as np
print("欢迎加入")
#数据处理库 
import pandas as pd
print("光环国际")
#可视化库
import matplotlib.pyplot as plt 
print("人工智能")
#深度学习框架   
import tensorflow as tf  
print("直通车")      
#机器学习包 PCA 算法
from sklearn.decomposition import PCA
print("学习班")
