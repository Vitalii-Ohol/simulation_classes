import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import math


NPoint=100
g=9.81
L=20.0
Ro=1
T0=1
dt=0.02


Amp = np.zeros([NPoint], dtype=np.float64)
Vel = np.zeros([NPoint], dtype=np.float64)
A = np.zeros([10], dtype=np.float64)
Fi = np.zeros([10], dtype=np.float64)
Exes = np.zeros([NPoint], dtype=np.float64)
Ek = 0.0
Ep = 0.0
eka = []
epa = []
eca = []
x=-10


for i in range(NPoint):
    Exes[i]=x
    x+=(20.0)/(NPoint-1.0)

start_p=4.0
Amp[int(NPoint/2)]=start_p
for i in range(1,4):
    Amp[int(NPoint/2-i)]=start_p
    Amp[int(NPoint/2+i)]=start_p
##    start_p+=.5


##for i in range(int(NPoint/2)):
##    Amp[i]=Amp[NPoint-i-1]=2.0*i/(NPoint/2.0);
##    Vel[i]=Vel[NPoint-i-1]=0.0;



fig, plotGrid = plt.subplots(2)

tmp1 = plotGrid[0].plot(Exes, [0]*NPoint)[0]
plotGrid[0].axes.get_xaxis().set_visible(False)
plotGrid[0].axes.get_yaxis().set_visible(False)
plotGrid[0].axis("equal")

tmp2 = plotGrid[1].plot([0]*NPoint, [0]*NPoint)[0]
tmp3 = plotGrid[1].plot([0]*NPoint, [0]*NPoint)[0]
tmp4 = plotGrid[1].plot([0]*NPoint, [0]*NPoint)[0]
plotGrid[1].axes.get_xaxis().set_visible(False)
plotGrid[1].axes.get_yaxis().set_visible(False)
##plotGrid[1].axis("equal")





def calc(i):
    global Vel, Amp, Ek, Ep
    #################################################################
    d2y = np.zeros([NPoint], dtype=np.float64)
    dx=1.0*L/(NPoint-1.0)
    dxdx=1.0*L/(NPoint-1.0)*L/(NPoint-1.0)

    d2y[0]=0
    d2y[(NPoint-1)]=0
    Ep=Ek=0.0
    for i in range(1, NPoint-1):
        d2y[i] = (Amp[i+1] + Amp[i-1] - 2 * Amp[i]) / dxdx
    Amp[0]=0.0
    Amp[NPoint-1]=0.0
    for i in range(1,NPoint):
        Vel[i] = Vel[i] + d2y[i]*dt
        Amp[i] = Amp[i] + Vel[i]*dt
        Ek += 1.0*(dx * Ro * Vel[i] * Vel[i] / 2)
        Ep += 1.0*(T0*((Amp[i]-Amp[i-1])*(Amp[i]-Amp[i-1]))/(2*dx))
    #################################################################

    tmp1.set_ydata(Amp)

    eka.append(Ek)
    epa.append(Ep)
    eca.append(Ek+Ep)
    
    plotGrid[1].set_xlim([len(eka)-60, len(eka)])
    tmp_max=max(max(eka), max(epa))
    tmp_max=max(tmp_max, max(eca))+1
    tmp_min=min(min(eka), min(epa))
    tmp_min=min(tmp_min, min(eca))-1
    plotGrid[1].set_ylim([tmp_min, tmp_max])
    

    tmp2.set_xdata(range(len(eka)))
    tmp2.set_ydata(eka)

    tmp3.set_xdata(range(len(epa)))
    tmp3.set_ydata(epa)

    
    tmp4.set_xdata(range(len(eca)))
    tmp4.set_ydata(eca)

    plt.draw()








a = anim.FuncAnimation(fig, calc, frames=200, repeat=True, interval=1)
plt.show()

