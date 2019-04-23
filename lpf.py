import numpy as np
from matplotlib import pyplot as plt
import cmath as mas
j=mas.sqrt(-1)
pi=3.14
T=0.1		#input("enter sampling time:")
ws=0.7*pi	#input("enter digital ws:")
wp=0.35*pi	#input("enter digital wp:")
dp=0.6		#input("enter passband ripples:")
ds=0.1		#input("enter stopband attenuation:")
def analog(w):
	W=(2.0/T)*np.tan(w*0.5)
	return W
Wp=analog(wp)
Ws=analog(ws)

x=np.log(((ds**(-2.0))-1)/((dp**(-2.0))-1))
y=np.log(Ws/Wp)
N1=0.5*(x/y)
N=np.ceil(N1)
y1=ds**(-2)
y2=(y1-1)**(1/(2*N))
Wc=Ws/y2
print Wc
k=1
hs=[]
x1=(2*k-1)*pi
x2=2*N
bk=2*np.sin(x1/x2)
print bk
w=np.arange(0,pi,0.01)
z=np.exp(j*w)
a=(z-1)
b=(1+z)
c=(a/b)
s=(2/T)*c
a1=((s**2)+(bk*Wc*s)+(Wc**2))
hs=(Wc**2)/(a1)
plt.grid()
plt.plot(w,np.abs(hs))
plt.show()
