import streamlit as st
import Lab1p1 as lab



def main():
    st.header("Menu de seniales", anchor=None)
    opciones=["--","Tren de pulsos","Cuadratica","Sinuidal","Triangular","Cuadrada","Lineal","Pulso","Exponencial"]
    sig=st.selectbox("", opciones)
    if sig!="--" and sig!="Tren de pulsos" and sig!="Pulso" and sig!="Cuadratica":
        f=st.number_input("Frecuencia (Hz)")
        if f/1==0:
            f=0.01
        t=lab.eje(f)
    if sig=="--":
        st.header("Bienvenido!")
        st.write("A continuacion dispone de un menu de ocho senales con las cuales puede "\
            "realizar las operaciones de desplazamiento en el tiempo, escalamietno en el tiempo y escalamiento en amplitud.")
    elif sig=="Tren de pulsos":
        lab.tren()
    elif sig=="Cuadratica":
        lab.cuadratica()
    elif sig=="Sinuidal":
        lab.seno(t,f)
    elif sig=="Triangular":
        lab.triangular(t,f)
    elif sig=="Cuadrada":
        lab.cuadrada(t,f)
    elif sig=="Pulso":
        ancho=st.number_input("Ingrese el ancho del pulso: ")
        alto=st.number_input("Ingrese el alto del pulso: ")
        lab.pulso(ancho,alto)
    elif sig=="Exponencial":
        lab.exponencial(t,f)
    elif sig=="Lineal":
        lab.lineal(t)
if __name__=="__main__":
    main()