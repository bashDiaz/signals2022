import os
import matplotlib.pyplot as plt
import numpy as np
os.system("cls")
t=np.arange(-3,3,0.001)
y=np.piecewise(t,[t>=-1, t<=1, t>1,t<-1],[1,1,0,0])
plt.plot(t,y)
plt.show()