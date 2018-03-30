#九九乘法表：
print('\n'.join(' '.join(list(map(lambda x: '%dx%d=%d'%(x,y,x*y), range(1,y+1)))) for y in range(1,10)))
