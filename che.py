import numpy as np
from matplotlib import pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
pi=3.14
dp=0.9	#0.6
ds=0.24	#0.1
Wp=0.25*pi#0.35*pi
Ws=0.5*pi#0.7*pi
T=1	#0.1
wp=(2/T)*np.tan(Wp/2)
ws=(2/T)*np.tan(Ws/2)
print wp
print ws
n1=cm.sqrt((ds**-2)-1)
n2=cm.sqrt((dp**-2)-1)
n3=n1/n2
n4=ws/wp
n5=np.arccosh(n3)
n6=np.arccosh(n4)
N1=n5/n6
N2=np.real(N1)
N=np.ceil(N2)
print "order(N)=",N
E1=cm.sqrt((dp**-2)-1)
E=np.real(E1)
print "epsilon=",E
a5=1/E**2
a6=a5+1
a1=cm.sqrt(a6)
a2=E**-1
a3=(a1+a2)**(1/N)
a4=(a1+a2)**(-1/N)
Yn=(0.5)*(a3-a4)
print "Yn=",Yn
k=1
bk1=(2*k-1)*pi
bk2=(2*N)
bk3=bk1/bk2
bk=2*Yn*np.sin(bk3)
print "bk=",bk
ck1=(Yn)**2
ck2=np.cos(bk3)
ck=ck1+(ck2*ck2)
print "ck=",ck
w=np.arange(0,pi,0.01)
z=np.exp(j*w)
s=(2/T)*((z-1)/(1+z))
b1=ck*pow(wp,N)
b4=dp*b1
b5=(s**2)+(bk*wp*s)+(ck*(wp*wp))
hs=b4/b5
plt.plot(w,np.abs(hs))
plt.grid()
plt.show()


