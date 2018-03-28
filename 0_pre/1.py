import numpy as np
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


      
np.random.seed(123)  
#x=np.random.randint(0,5,[2,3])  
x = np.random.randint(0 , 5, [3,2,4])
print("原始数组为:")
print(x)

for i in range(3):
    print("x.max(axis="+ str(i) +"):")
    print(x.max(axis=i))

"""
a=[[1,2,3],
   [4,5,6]]
print("列表a如下：")
print(a)

   
print("增加一维，新维度的下标为0")
c=np.stack(a,axis=0)
print(c)

print("增加一维，新维度的下标为1")
c=np.stack(a,axis=1)
print(c)
"""