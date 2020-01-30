import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def calc(m, k):
    dt = .1
    gx = 0
    gy = -10

    sx = [0]
    sy = [0]
    vx = [10]
    vy = [10]

    while(sy[-1]>=0):
        ax = (m*gx - k*vx[-1])/m
        ay = (m*gy - k*vy[-1])/m

        vx2 = vx[-1] + ax*dt/2
        vy2 = vy[-1] + ay*dt/2

        ax2 = (m*gx - k*vx2)/m
        ay2 = (m*gy - k*vy2)/m

        dsx = vx2*dt
        dsy = vy2*dt
        dvx = ax2*dt
        dvy = ay2*dt

        sx.append(sx[-1]+dsx)
        sy.append(sy[-1]+dsy)
        vx.append(vx[-1]+dvx)
        vy.append(vy[-1]+dvy)
    return sx, sy


m = 100
k = 200
sx, sy = calc(m, k)
fig, ax = plt.subplots()
plt.subplots_adjust(left=.1, bottom=.25)
l, = plt.plot(sx, sy)

axfreq = plt.axes([0.1, 0.1, 0.75, 0.03])
axamp = plt.axes([0.1, 0.15, 0.75, 0.03])
sm = Slider(axfreq, 'm', 0, 1000, valinit=m)
sk = Slider(axamp, 'k', 0, 1000, valinit=k)
def update(val):
    m_new = sm.val
    k_new = sk.val
    sx, sy = calc(m_new, k_new)
    l.set_xdata(sx)
    l.set_ydata(sy)
    fig.canvas.draw_idle()
sm.on_changed(update)
sk.on_changed(update)

plt.show()
