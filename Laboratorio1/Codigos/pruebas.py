import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axis as ax
os.system("cls")
am=1
des=3
esc=(9/3)
# t=np.arange(-4,4,0.001)
# y=np.piecewise(t,[t>=-1, t<=1, t>1,t<-1],[1,1,0,0])
# y2=np.piecewise(t,[t>=-2, t<=2, t>2,t<-2],[2,2,0,0])
# y3=np.piecewise(t,[t>=-3, t<=3, t>3,t<-3],[1,1,0,0])
# y4=np.piecewise(t,[t>=-2, t<=2, t>2,t<-2],[4,4,0,0])
# frames=20
# t2=(t-des)/esc
# y2=y*am
t=[1,2,3,4,5]
y=[4,2,1,2,3]
print(t[len(t)-1])
y3=[]
t3=[]
y4=[]
t4=[]
if abs(esc)>1:
    for i in range(len(t)):
        if round((t[i]/esc))==(t[i]/esc):
            y3.append(y[i])
            t3.append((t[i]/esc))
else:
    tesc=[i/esc for i in t]
    for i in range(int(tesc[(len(tesc)-1)]+1)):
        t3.append(i)
    print(int(tesc[(len(tesc)-1)]))
    print(len(t3))
    y3=[0 for i in t3]
    print(y3)
    for i in range((len(t))):
        for j in range(len(t3)):
            print("iteracion j : {}".format(j))
            print("iteracion i : {}".format(i))
            if t3[j]==t[i]/esc:
                print("Entro {}".format(t3[j]))
                y3[t3[j]]=y[i]
                print(y3)
print(t3)
print(y3)
# frames = 10
# for i in range(frames+1):
#     print(i)
#     t4=t+t3*(i/frames)-(t*i/frames)
#     y4=y+y3*(i)/frames-(y*i/frames)
#     plt.plot(t,y)
#     plt.plot(t4,y4)
#     plt.show()

# fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)
# ax1.plot(t,y)
# ax1.set_title("imagen 1",y=-.24)
# ax1.get_title()
# ax2.plot(t,y2)
# ax2.set_title("imagen 2")
# ax3.plot(t,y3)
# ax3.set_title("imagen 3",y=-.25)
# ax4.plot(t,y4)
# ax4.set_title("imagen 4")
# fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)
# ax1.plot(t*2,y)
# ax1.set_title("imagen 1",y=-.24)
# ax1.get_title()
# ax2.plot(t*2,y2)
# ax2.set_title("imagen 2")
# ax3.plot(t*2,y3)
# ax3.set_title("imagen 3",y=-.25)
# ax4.plot(t*2,y4)
# ax4.set_title("imagen 4")
# plt.show()



# # plt.plot(t,y)
# # plt.show()
# import os

# # os.system("cls")
# # y=[h for h in t if round((am*(h-des)/esc))==(am*(h-des)/esc)]
# # t=[((am*(j-des))/esc) for j in t if round((am*(j-des)/esc))==(am*(j-des)/esc)]
# # y=[j for j in y if j!=None]
# # t=[j for j in t if j!=None]
# t="1,2,2,10"
# y="1,2,3,4"
# t=t.split(",")
# print(t)
# t=[int(i) for i in t]
# print(t)
# y=y.split(",")
# print(y)
# j=[]
# t2=[]
# y=[int(i) for i in y if i!=" "]
# t=[int(i) for i in t if i!=" "]
# for i in range(len(t)):
#     if round(am*(t[i]-des)/esc)==am*(t[i]-des)/esc:
#         j.append(y[i])
#         t2.append(am*(t[i]-des)/esc)
# y=[y[t.index(h)] for h in t if round((am*(h-des)/esc))==(am*(h-des)/esc)]
# t=[((am*(j-des))/esc) for j in t if round((am*(j-des)/esc))==(am*(j-des)/esc)]
# # print(t2)
# # print(j)
# # print(t)
# # print(y)
# fig,ax=plt.subplots()
# ax.plot(t2,j)
# plt.show()