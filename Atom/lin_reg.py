import pandas as pd
import numpy as np

x = [1.0,1.6,3.4,4.0,5.2]
y = [1.2,2.0,2.4,3.5,3.5]
yi = [1.2,3.2,8.16,14.0,18.2]
y2 = [1.0,2.56,11.56,16.0,27.04]



#print (suma(x))
#print (suma(y))


#x1 = np.array([x])
#y1 = np.array([y])


#xy = x1*y1

#x2 = x1*x1

#n = len(x)


def suma(x):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
    return sum
def suma2(x):  #x*x
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
    return sum

def suma3(x):   #x*y
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
    return sum

def lin_reg(m,n):
    n = len(m)
    x = np.array([m])
    y = np.array([n])
    x2 = x*x
    xy = x*y
    sumx2= pow(suma(x),2)
    sum11b= suma(x)*n
    sum1b = sum11b*suma(x2)
    sum2b= suma(xy)*suma(x)
    rest1b= sum1b-sum2b
    rest2b= suma(x2)*n
    rest3b= rest2b-sumx2
    div1b= rest1b/rest3b
    return div1b

print (lin_reg(x,y))
