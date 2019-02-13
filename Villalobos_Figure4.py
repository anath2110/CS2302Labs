'''
    Code created and Modified by: Ismael Villalobos
    Skeleton code provide by: Olac Fuentes
    Date:2/12/19
    Lab1
'''
import matplotlib.pyplot as plt
import numpy as np
import math


def circle(center, rad):
    n = int(2 * rad * math.pi)
    t = np.linspace(0, 6.3, n)
    x = center[0] + rad * np.sin(t)
    y = center[1] + rad * np.cos(t)
    print(x)
    print(y)
    ax.plot(x, y,linewidth=0.75, color='k')
    return x, y


def draw_circles(ax, n, center, radius):
    if n > 0:
        circle(center, radius)

        point1 = [center[0] + (radius * (2 / 3)), center[1]]
        point2 = [center[0] - (radius * (2 / 3)), center[1]]
        point3 = [center[0], center[1] - (radius * (2 / 3))]
        point4 = [center[0], center[1] + (radius * (2 / 3))]

        draw_circles(ax, n - 1, center, radius * (1 / 3))
        draw_circles(ax, n - 1, point1, radius * (1 / 3))
        draw_circles(ax, n - 1, point2, radius * (1 / 3))
        draw_circles(ax, n - 1, point3, radius * (1 / 3))
        draw_circles(ax, n - 1, point4, radius * (1 / 3))


plt.close('all')
fig, ax = plt.subplots()
ax.set_aspect(1.0)
ax.axis('off')
draw_circles(ax, 3, [0, 0], 50)
plt.show()
fig.savefig('circleFlower1.png')

plt.close('all')
fig, ax = plt.subplots()
ax.set_aspect(1.0)
ax.axis('off')
draw_circles(ax, 4, [0, 0], 50)
plt.show()
fig.savefig('circleFlower2.png')

plt.close('all')
fig, ax = plt.subplots()
ax.set_aspect(1.0)
ax.axis('off')
draw_circles(ax, 5, [0, 0], 50)
plt.show()
fig.savefig('circleFlower3.png')



