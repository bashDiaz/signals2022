import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg
import streamlit as st

def conf(a,b,c=1):
        a.set_markerfacecolor("none")
        a.set_markeredgecolor("violet")
        b.set_linestyle("--")
def start(con,ver=1):
    if st.checkbox("Transformacion de senales"):
        if ver==1:
            con[0]=st.number_input("Introduzca el valor a desplazar en el tiempo")
        if ver==2:
            con[0]=st.number_input("Introduzca el valor a desplazar en el tiempo",step=1)
        con[1]=st.number_input("Introduza el valor a escalar en el tiempo")
        con[2]=st.number_input("Introduzca el valor a esclaar en amplitud")
def graficar(t,y):
    con=[0,0,0]
    fig, ax=plt.subplots()
    ax.plot(t,y)
    st.pyplot(fig)
    start(con)
    if con[0]!=0 or con[1]!=0 or con[2]!=0:
        if con[1]==0:
            con[1]=1
        plotfig  = st.empty()
        tdes=t-con[0]
        tesc=t/con[1]
        yesc=y*con[2]
        t2=(t-con[0])/con[1]
        frames=20
        for i in range(frames+1):
            fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)
            ax1.plot(t,y)
            ax2.plot(t,y)
            ax3.plot(t,y)
            ax4.plot(t,y)
            tgen=t+t2*(i/frames)-t*(i/frames)
            ygen=y+yesc*(i/frames)-y*(i/frames)
            tdes2=t+tdes*(i)/frames-(t*i/frames)
            tesc2=t+tesc*(i)/frames-(t*i/frames)
            yesc2=y+yesc*(i)/frames-(y*i/frames)
            ax1.plot(tgen,ygen,linestyle="dashed")
            ax1.legend(["Original","Transformada Total"])
            ax2.plot(tdes2,y,linestyle="dashed")
            ax2.legend(["Original","Desplazada"])
            ax3.plot(tesc2,y,linestyle="dashed")
            ax3.legend(["Original","Escalada en el tiempo"])
            ax4.plot(t,yesc2,linestyle="dashed")
            ax4.legend(["Original","Escalada en amplitud"])
            plotfig.pyplot(fig)
def amplitud():
    return (st.number_input("Introduzca el valor de amplitud A: "))
def discreta(t,y):
    con=[0,0,0]
    fig, ax=plt.subplots()
    ax.stem(t,y)
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    tt=[]
    st.pyplot(fig)
    start(con,2)
    if con[0]!=0 or con[1]!=0 or con[2]!=0:
        if con[1]==0:
            con[1]=1
        plotfig  = st.empty()
        fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)
        ax1.stem(t,y)
        ax2.stem(t,y)
        ax3.stem(t,y)
        ax4.stem(t,y)
        for i in range(len(t)):
            tt.append(t[i]-con[0])
        if abs(con[1])>1:
            for i in range(len(tt)):
                if round((tt[i]/con[1]))==(tt[i]/con[1]):
                    y1.append(y[i])
                    t1.append((tt[i]/con[1]))
            st.write("y1= {}  y={}".format(y1,y))        
        else:
            tesc=[i/con[1] for i in tt]
            for i in range(int(tesc[(len(tesc)-1)]+1)):
                t1.append(i)
            y1=[0 for i in t1]
            for i in range((len(tt))):
                for j in range(len(t1)):
                    if t1[j]==tt[i]/con[1]:
                        y1[t1[j]]=y[i]
        y1=[i*con[2] for i in y1]
        markerline, stemlines, baseline = ax1.stem(t1,y1,linefmt="Violet",markerfmt="D")
        conf(markerline,stemlines,baseline)
        ax1.legend(["Original","Transformada Total"])
        for i in range(len(t)):
            if round((t[i]-con[0])==(t[i]-con[0])):
                y2.append(y[i])
                t2.append((t[i]-con[0]))
        markerline2, stemlines2, baseline = ax2.stem(t2,y2,linefmt="Violet",markerfmt="D")
        conf(markerline2,stemlines2,baseline)
        ax2.legend(["Original","Desplazada"])
        if abs(con[1])>1:
            for i in range(len(t)):
                if round((t[i]/con[1]))==(t[i]/con[1]):
                    y3.append(y[i])
                    t3.append((t[i]/con[1]))
        else:
            tesc=[i/con[1] for i in t]
            for i in range(int(tesc[(len(tesc)-1)]+1)):
                t3.append(i)
            y3=[0 for i in t3]
            for i in range((len(t))):
                for j in range(len(t3)):
                    if t3[j]==t[i]/con[1]:
                        y3[t3[j]]=y[i]
        markerline3, stemlines3, baseline = ax3.stem(t3,y3,linefmt="Violet",markerfmt="D")
        conf(markerline3,stemlines3,baseline)       
        ax3.legend(["Original","Escalada en el tiempo"])  
        y4=[i*con[2] for i in y] 
        t4=t
        markerline4, stemlines4, baseline = ax4.stem(t4,y4,linefmt="Violet",markerfmt="D")
        conf(markerline4,stemlines4,baseline)
        ax4.legend(["Original","Escalada en amplitud"])
        plotfig.pyplot(fig)
def eje(f):
    inicial=-1/(f)
    final=(1/f)
    t=np.arange(inicial,final,(1/(10*2*np.pi*f)))
    return(t)
#Se crea la signal triangular  1
def triangular(t,f):
    a=amplitud()
    y=sg.sawtooth(2*np.pi*t*f)*a
    graficar(t,y)
#Se genera la signal cuadrada 2
def cuadrada(t,f):
    a=amplitud()
    y=sg.square(t*f*2*np.pi)*a
    graficar(t,y)
#Se genera la signal exponencial 3
def exponencial(t):
    a=amplitud()
    b=st.number_input("Introduzca el valor de b: ")
    y=(np.exp(-b*t))*a
    graficar(t,y)
#Se genera la signal sinuidal 4
def seno(t,f):
    a=amplitud()
    y=np.sin(f*t*2*np.pi)*a
    graficar(t,y)
#Se genera la signal pulso 5
def pulso(ancho,alto):
    t=np.arange(-ancho,ancho,0.01)
    y=np.piecewise(t,[(t)>=(-ancho/2),(t)<=(ancho/2),(t)>ancho/2,(t)<-ancho/2],[alto,alto,0,0])
    graficar(t,y)
#Se crea la signal cuadratica 6
def cuadratica():
    a=st.number_input("Introduzca el valor de a: ")
    b=st.number_input("Introduzca el valor de b: ")
    c=st.number_input("Introduzca el valor de c: ")
    if b==0:
        t=np.arange(-1,1,0.01)
    else:
        t=np.arange((-b*2),b,0.01)
    y=(a*((t))**2)+(b*t)+c
    graficar(t,y)
#Se crea la signal lineal 7
def lineal(t):
    m=st.number_input("Introduzca el valor de la pendiente m: ")
    b=st.number_input("Introduzca el valor de b: ")
    y=m*t+b
    graficar(t,y)
#se define el tren de pulsos en dominio discreto 8
def tren():
    y =st.text_input("Introduzca los valores de amplitud los pulsos separado por coma ','","0,0,0,0,0")
    y=y.split(",")
    y=[int(i) for i in y]
    t=st.text_input("Introduzca la posicion de los pulsos separado por coma ','", "1,2,3,4,5")
    t=t.split(",")
    t=[int(i) for i in t]
    if len(t)!=len(y):
        st.title("Alerta!")
        st.write("Los vectores de posicion y amplitud no tienen el mismo numero de componentes, "\
             "por favor iguale la cantidad de componentes de los mismos para poder realizar la grafica.")
    else: 
        discreta(t,y) 
#Funcion principal
def main():
    os.system("cls")
if __name__=="__main__":
    main()