import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,3,100)
plt.rcParams["font.sans-serif"]=["SimHei"]
y=-np.cos(2*x*np.pi)
np.sin(x)
plt.xticks(np.linspace(0,3,7))
plt.plot(x,y)
plt.ylabel("Potential V(x)")
plt.scatter([0.5,1.5,2.5],[0,0,0],c="r",s=200)
plt.legend(["potential 势能 V(x)","原子位置 atom position"],loc="center right")
plt.savefig(r".\pic\pic1.jpg")
plt.cla()




plt.plot(x,y)

z=np.sin(2*np.pi*x/3)
a=np.sin(4*np.pi*x/3)
b=np.sin(6*np.pi*x/3)

plt.plot(x,z*y)
plt.plot(x,a*y)
plt.plot(x,b*y)
plt.xticks(np.linspace(-0,3,7))
plt.scatter([0.5,1.5,2.5],[0,0,0],c="r",s=200)
plt.legend(["k=0 or v(x)","k=2pi/3a","k=4pi/3a","k=2pi","atom"],loc="lower right")

plt.savefig(r".\pic\pic2.jpg")