import numpy as np
from matplotlib import pyplot as plt
import cmath as mas
j=mas.sqrt(-1)
pi=3.14
T=0.1		#input("enter sampling time:")
ws1=160*pi
wp1=400*pi	#input("enter digital ws:")
wp2=1200*pi
ws2=3000*pi	#input("enter digital wp:")
dp=0.6		#input("enter passband ripples:")
ds=0.1		#input("enter stopband attenuation:")
def analog(w):
	W=(2.0/T)*np.tan(w*0.5)
	return W
#Wp1=analog(wp1)
#Ws1=analog(ws1)
#Ws2=analog(ws2)
#Wp2=analog(wp2)
Ws1=160*pi
Wp1=400*pi
Wp2=1200*pi
Ws2=3000*pi 
Wp3=1
Ws3=(Ws2-Ws1)/(Wp2-Wp1)
print Ws3
x=np.log(((ds**(-2.0))-1)/((dp**(-2.0))-1))
y=np.log(Ws3/Wp3)
N1=0.5*(x/y)
N=np.ceil(N1)
print N
y1=ds**(-2)
y2=(y1-1)**(1/(2*N))
Wc=Ws3/y2
print Wc
k=1
hs=[]
x1=(2*k-1)*pi
x2=2*N
bk=2*np.sin(x1/x2)
print bk
w=np.arange(0,12000,1)
#z=np.exp(j*w)
#a=(z-1)
#b=(1+z)
#c=(a/b)
#s=(2/T)*c
s=j*w
B=wp2-wp1
w0=mas.sqrt(wp1*wp2)
f=(s**2+w0**2)
g=(B*s)
s1=f/g
a1=((s1**2)+(bk*Wc*s1)+(Wc**2))
hs1=(Wc**2)/(a1)
plt.grid()
plt.plot(w,np.abs(hs1))
plt.show()


