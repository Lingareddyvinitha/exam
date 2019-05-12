import numpy as np
import matplotlib.image as mpimg 
from matplotlib import pyplot as plt 
from matplotlib import pyplot as plt
from scipy import signal
p=input("enter the order of the moving average system")
x = mpimg.imread('NOISY_Lena.png') 
m=len(x)
n=len(x[0])
print m,n
y=[]
x3=[]
for i in range(0,250,1):
	for j in range(0,200,1):
		a=x[i][j]
		y.append(a)
	sum=0
	y2=[]
	for i in range(0,len(y),1):
		for k in range(0,p-1,1):
			sum=sum+y[i-k]
		y2.append(float((sum)/(p)))
		sum=0
	x3.append(y2)
	y=[]
	y2=[]
plt.subplot(211)
plt.imshow(x)
plt.subplot(212)
plt.imshow(x3)
plt.show()
