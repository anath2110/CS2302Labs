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
    return x, y


def draw_circles(ax, n, center, radius, w):
    if n > 0:
        x, y = circle(center, radius)
        ax.plot(x, y, color='k')
        radius = radius * w
        center = [radius,0]
        draw_circles(ax, n - 1, center, radius, w)


plt.close("all")
fig, ax = plt.subplots()
draw_circles(ax, 25, [100, 0], 100, .6)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')

plt.close("all")
fig, ax = plt.subplots()
draw_circles(ax, 50, [100, 0], 100, .9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles1.png')

plt.close("all")
fig, ax = plt.subplots()
draw_circles(ax, 85, [100, 0], 100, .95)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles2.png')