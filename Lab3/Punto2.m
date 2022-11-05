clc
clear all
N = abs(input('Ingrese el numero de muestras: '));
n = 0:N-1;
fs = abs(input('Ingrese la frecuencia 0: '));
fs1 = abs(input('Ingrese la frecuencia 1: '));
fs2 = abs(input('Ingrese la frecuencia 2: '));
t = 0:1/fs:1;
w0 = fs*2*pi;
w1 = fs1*2*pi;
w2 = fs2*2*pi;
A0 = abs(input('Ingrese la Amplitud 0: '));
A1 = abs(input('Ingrese la Amplitud 1: '));
A2 = abs(input('Ingrese la Amplitud 2: '));

x1 = A0*sin(w0*n/fs) + A1*cos(w1*n/fs) + A2*sin(w2*n/fs);

y = fft(x1);
sp_fft = abs(fftshift(y));
f1 = (-0.5:1/length(sp_fft):0.5-(1/length(sp_fft)))*fs;
figure(1)
subplot(2,1,1), plot(n,x1);
subplot(2,1,2), plot(f1,sp_fft);
figure(2)
subplot(2,1,1), stem(n,x1);
subplot(2,1,2), stem(f1,sp_fft);