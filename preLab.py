import numpy as np
import matplotlib.pyplot as plt
import os
os.system("cls")
f=int(input("Ingrese la frecuencia: "))
a=int(input("Ingrese el valor de amplitud: "))
t=np.arange(0,2*np.pi,0.01)
print("La frecuencia es {}".format(f))
print("La amplitud  es {}".format(a))
y=np.sin(2*np.pi*f*t)*a
plt.plot(t,y)
plt.show()