import matplotlib.pyplot as plt
import numpy as n
import math
# from matplotlib.widgets import Slider

l=3
m = 1
g = 10
n = 1000
dt = .1

def calc(n, advanced = 1):
    startAlpha = (120 % 360) / 180 * math.pi
    alpha = [startAlpha]
    omega = [0]
    e = []
    e.append(m*g/l*math.sin(alpha[0]))

    x = []
    y = []
    ek = []
    ep = []

    for i in range(1, n):
        x.append(l*math.sin(alpha[-1]))
        y.append(l*math.cos(alpha[-1])+l)
        ek.append(m*(omega[-1]**2)*(l**2)/2)
        ep.append(m*g*y[-1])
        if advanced == 1:
            omega2 = omega[-1] + e[-1]*dt/2
            alpha2 =alpha[-1] + omega[-1]*dt/2
            e2 = m*g/l*math.sin(alpha2)  
        else:
            omega2 = omega[-1]
            e2 = e[-1]
            alpha2 = alpha[-1]
        alpha.append(alpha[-1] + omega2*dt)
        omega.append(omega[-1] + e2*dt)
        e.append(m*g/l*math.sin(alpha2))
    return x,y,ek,ep



fig, plotGrid = plt.subplots(2,2)
plt.subplots_adjust(left=.05, bottom=.05, right=.95, top=.95)
title = 'Euler'
for step in range(2):
    x,y,ek,ep = calc(n, step)
    ex = range(1, n)
    #ex=np.linspace(0, kr*dt, kr-1)

    plotGrid[0,step].plot(x,y)
    plotGrid[0,step].set_title(title)
    plotGrid[0,step].axis('equal')
    plotGrid[0,step].grid()

    plotGrid[1,step].plot(ex, ek, label = 'kinetical')
    plotGrid[1,step].plot(ex, ep, label = 'potential')
    plotGrid[1,step].grid()
    plotGrid[1,step].legend(fancybox=True)
    title += ' '
    title += 'advanced'


plt.show()
