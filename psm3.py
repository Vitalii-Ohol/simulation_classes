import matplotlib.pyplot as plt
# import numpy as np
from math import sin, cos
from matplotlib.widgets import Slider

def calc(m, l, n, g, startAlpha, startOmega):
    dt = .1
    # g = 10
    alpha = []
    alpha.append(startAlpha)
    omega = []
    omega.append(startOmega)
    energyN = []
    energyP = []
    x = []
    y = []

    for i in range(1, n):
        x.append(l*sin(alpha[-1]))
        y.append(l*cos(alpha[-1]))
        energyN.append((m*omega[-1]**2*l**2)/2)
        h = l-cos(alpha[-1])
        energyP.append(m*g*h)

        exp = (m*g*sin(alpha[-1]))/l
        alpha2 = alpha[-1]+omega[-1]*dt/2;
        omega2 = omega[-1] + exp*dt/2
        exp2 = (m*g*sin(alpha2))/l
        dalpha = omega2*dt
        domega = exp2*dt
        alpha.append(alpha[-1]+dalpha)
        omega.append(omega[-1]+domega)
    return x, y, energyN, energyP


m = 100
l = 200
n = 1000
g = 10
startAlpha = 60
startOmega = 0
x, y, energyN, energyP = calc(m, l, n, g, startAlpha, startOmega)
fig = plt.figure()
ax1 = fig.add_subplot(211, aspect='auto')
la1, = ax1.plot(x, y)
ax2 = fig.add_subplot(212, aspect='auto')
la2, = ax2.plot(range(1,n), energyN)
la3, = ax2.plot(range(1,n), energyP)
# ax2.set_xlim(xmin=0)
# x2.set_ylim(ymin=0)
fig.subplots_adjust(left=.1, bottom=.45)


axm = plt.axes([0.1, 0.10, 0.75, 0.03])
axl = plt.axes([0.1, 0.15, 0.75, 0.03])
axn = plt.axes([0.1, 0.20, 0.75, 0.03])
axg = plt.axes([0.1, 0.25, 0.75, 0.03])
axstartAlpha = plt.axes([0.1, 0.30, 0.75, 0.03])
axstartOmega = plt.axes([0.1, 0.35, 0.75, 0.03])
sm = Slider(axm, 'm', 0, 1000, valinit=m)
sl = Slider(axl, 'l', 0, 1000, valinit=l)
sn = Slider(axn, 'n', 0, 10000, valinit=n, valstep=1)
sg = Slider(axg, 'g', 0, 1000, valinit=g, valstep=1)
sstartAlpha = Slider(axstartAlpha, 'startAlpha', 0, 1000, valinit=startAlpha, valstep=1)
sstartOmega = Slider(axstartOmega, 'startOmega', 0, 1000, valinit=startOmega, valstep=1)
def update(val):
    m_new = sm.val
    l_new = sl.val
    n_new = sn.val
    n_new = n_new.astype(int)
    g_new = sg.val
    # g_new = g_new.astype(int)
    startAlpha_new = sstartAlpha.val
    # startAlpha_new = startAlpha_new.astype(int)
    startOmega_new = sstartOmega.val
    # startOmega_new = startOmega_new.astype(int)
    x, y, energyN, energyP = calc(m_new, l_new, n_new, g_new, startAlpha_new, startOmega_new)
    la1.set_xdata(x)
    la1.set_ydata(y)
    la2.set_xdata(range(1, n_new))
    la2.set_ydata(energyN)
    la3.set_xdata(range(1, n_new))
    la3.set_ydata(energyP)
    # axx = plt.gca()
    # axx.relim()
    # axx.autoscale_view()
    ax1.autoscale()
    ax2.autoscale()
    fig.canvas.draw_idle()
sm.on_changed(update)
sl.on_changed(update)
sn.on_changed(update)
sg.on_changed(update)
sstartAlpha.on_changed(update)
sstartOmega.on_changed(update)




plt.show()
