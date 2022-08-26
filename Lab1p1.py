import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg


def amplitud():
    return (int(input("Introduzca el valor de amplitud A: ")))
def continua(t,y):
    plt.plot(t,y)
    plt.show()
def discreta(t,y):
    plt.stem(t,y)
    plt.show()
def eje(f,inicial=-5,final=2*np.pi):
    t=np.arange(inicial,final,(1/(2*np.pi*f)))
    return(t)
#Se crea la signal triangular  1
def triangular(t):
    a=amplitud()
    y=sg.sawtooth(2*np.pi*t*1)*a
    continua(t,y)
#Se genera la signal cuadrada 2
def cuadrada(t):
    a=amplitud()
    y=sg.square(2*np.pi*t*1)*a
    continua(t,y)
#Se genera la signal exponencial 3
def exponencial(t):
    a=amplitud()
    b=int(input("Introduzca el valor de b: "))
    y=np.exp(-b*t)*a
    continua(t,y)
#Se genera la signal sinuidal 4
def seno(t,f=1):
    a=amplitud()
    y=a*np.sin(2*np.pi*f*t)
    continua(t,y)
#Se genera la signal pulso 5
def pulso(t,des=0,esc=1,amp=1):
    start=int(input("Ingrese punto inicial: "))
    end=int(input("Ingrese punto final: "))
    a=amplitud()
    y=np.piecewise(t,[(t)>=start,(t)<=end,(t)>end,(t)<start],[a,a,0,0])
    continua((amp*((t-des)/esc)),y)
#Se crea la signal cuadratica 6
def cuadratica(t,des=0,esc=1,am=1):
    a=int(input("Introduzca el valor de a: "))
    b=int(input("Introduzca el valor de b: "))
    c=int(input("Introduzca el valor de c: "))
    y=(a*((t))**2)+(b*t)+c
    continua(am*((t-des)/esc),y)
#Se crea la signal lineal 7
def lineal(t):
    m=int(input("Introduzca el valor de la pendiente m: "))
    b=int(input("Introduzca el valor de b: "))
    y=m*t+b
    continua(t,y)
#se define el tren de pulsos en dominio discreto 8
def tren(t):
    a=amplitud()
    y=np.ones(len(t))*a
    discreta(t,y)  
#Funcion principal
def main():
    os.system("cls")
    f=5 #int(input("Introduzca el valor de frecuencia f: "))
    t=eje(f)

if __name__=="__main__":
    main()