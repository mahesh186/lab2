import numpy as np
from matplotlib import pyplot as plt
import cmath as mas
W=[]
j=mas.sqrt(-1)
M=input("enter no.of samples:")
for n in range(0,M):
	wa=0.42-0.5*np.cos((2.0*np.pi*n)/(M-1.0))+0.08*np.cos((4.0*np.pi*n)/(M-1.0))
	W.append(wa)
plt.subplot(2,3,1)
plt.stem(W)
plt.title('black man window')
h=[]
fc=np.pi/4
n=np.linspace(-100,100,200)
print n
h=np.append(h,((np.sin(fc*n))/(np.pi*n)))
plt.subplot(2,3,2)
plt.stem(n,h)
plt.title('sinc function')
def dtft(x):
	N=len(x)
	y=[]
	w=np.linspace(-np.pi,np.pi,100)
	for i in range (0,100):
		sum=0
		for n in range (0,N,1):
			sum=sum+x[n]*np.exp(-j*w[i]*n)
		y.append(sum)
	return y
y=dtft(h)
plt.subplot(2,3,3)
plt.stem(np.abs(y))
plt.grid()
plt.title('dtft of sinc')
z=len(W)
f=len(h)
hn=[]
fc=np.pi/4
n=np.arange(-20,20,1)
print n
'''hn=np.append(hn,((np.sin(fc*n))/(np.pi*n)))'''
hn=np.append(hn,(.25*np.sinc(.25*n)))

hd=[]
for k in range(0,min(z,f)):
	hd1=W[k]*hn[k]
	hd.append(hd1)
plt.subplot(2,3,4)
plt.stem(hd)
plt.title('mul.of bmw&sinc')
g=dtft(hd)
plt.subplot(2,3,5)
plt.plot(np.abs(g))
plt.title('dtft of mul')
plt.subplot(2,3,6)
plt.plot(20*np.log(g))
plt.title('db plot')
plt.grid()
plt.show()
























