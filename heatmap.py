import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter



NX=30
divx=NX
divy=NX
dim=NX*NX

grid = np.zeros((divx, divy))
grid[:, divy-1] = 200.0;
grid[:, 0] = 150.0;
grid[0, :] = 100.0
grid[divx-1, :] = 50.0
#print(grid)

top=100.0
bottom=50.0
left=150.0
right=200.0

mat = np.zeros((dim, dim))
b = np.zeros((dim,))


for y in range(divy):
    for x in range(divx):
        mat[x + y*divx, x + y*divx] = -4.0
        if x == 0:
            b[y*divx + x] -= left
        else:
            mat[x + y*divx, x + y*divx -1] = 1.0
        if x == divx-1:
            b[y*divx + x] -= right
        else:
            mat[x + y*divx, x + y*divx + 1] = 1.0

        if y == 0:
            b[y*divx + x] -= bottom
        else:
            mat[x + y*divx, x + (y-1)*divx ] = 1.0

        if y == divy-1:
            b[y*divx + x] -= top
        else:
            mat[x + y*divx, x + (y+1)*divx ] = 1.0
        #b[y*divx + x] -= grid[y,x]


print(mat)
print(b.reshape((NX,NX)))



Z = np.linalg.inv(mat).dot(b)
Z = Z.reshape(divx, divy)

X = np.linspace(1, divx, divx)
Y = np.linspace(1, divy, divy)
X, Y = np.meshgrid(X, Y)


fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap="viridis", linewidth=0, antialiased=False)

ax.set_zlim(50, 200)
ax.zaxis.set_major_locator(LinearLocator(6))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))

fig.colorbar(surf, shrink=0.5, aspect=9)

plt.show()
