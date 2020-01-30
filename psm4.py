import matplotlib.pyplot as plt
import numpy as np
import math
# from matplotlib.widgets import Slider
plt.style.use('ggplot')




n = 600
dt = 0.01
m = 1.0
g = 10.0
r = 2.0
alpha = 30.0
wysokosc = 30.0
alphaRadian = (alpha % 360) / 180 * np.pi


num = 2

baseI = m * r**2
brylaNazwa = ['Kula 2/5', 'Walec 1/2', 'sfera 2/3']
brylaW = [2.0 / 5, 1.0 / 2, 2.0/3]
brylaI = [baseI*x for x in brylaW]
brylaMn = [1.0/(1+x) for x in brylaW]
brylaA = [x*g*np.sin(alphaRadian) for x in brylaMn]
ep = [x/r for x in brylaA]


fig, plotGrid = plt.subplots(2,num)
plt.subplots_adjust(left=.05, bottom=.05, right=.95, top=.95)

for id in range(num):
    szybkosc = np.zeros((n, ), dtype=float)
    szybkosc[0]=0
    droga = np.zeros((n, ), dtype=float)
    droga[0]=0


    omega = np.zeros((n, ), dtype=float)
    beta = np.zeros((n, ), dtype=float)
    ek = np.zeros((n, ), dtype=float)
    omega[0]=0
    beta[0]=0
    ek[0]=0

    koniec=n
    for moment in range(1, n):
        szybkoscPol = szybkosc[moment-1]+brylaA[id]*dt/2
        szybkosc[moment] = szybkosc[moment-1] + brylaA[id]*dt
        droga[moment]= droga[moment-1]+szybkoscPol*dt

        omegaPol = omega[moment-1]+ep[id]*dt/2
        omega[moment] = omega[moment-1]+ep[id]*dt
        beta[moment] = beta[moment-1]+omegaPol*dt
        ek[moment] = m * szybkosc[moment]**2 / 2 + brylaI[id]*omega[moment]**2 / 2

        if wysokosc - droga[moment] * np.sin(alphaRadian) <=0:
            koniec = moment
            break

    x = droga * np.cos(alphaRadian)
    y = wysokosc + r - droga*np.sin(alphaRadian)
    epot = (y-r)*g*m

    xcy = x+r*np.sin(beta)
    ycy = y+r*np.cos(beta)
    ex = np.linspace(0, koniec*dt, koniec)

    
    plotGrid[0,id].plot(ex,epot[:koniec], label='potential')
    plotGrid[0,id].plot(ex,ek[:koniec], label='kinetic')
    plotGrid[0,id].legend(fancybox=True)
##    tmp = ek+epot
##    plotGrid[0,id].plot(ex,tmp[:koniec])

    plotGrid[1,id].plot(x, y)
    plotGrid[1,id].plot(xcy[:koniec], ycy[:koniec])
    plotGrid[1,id].set_title(brylaNazwa[id])
    plotGrid[1,id].axis('equal')

    del x
    del y
    del epot
    del xcy
    del ycy
    del ex
    del szybkosc
    del droga
    del omega
    del beta
    del ek
    

plt.show()
