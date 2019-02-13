'''
    Code created and Modified by: Ismael Villalobos
    Skeleton code provide by: Olac Fuentes
    Date:2/12/19
    Lab1
'''
import numpy as np
import matplotlib.pyplot as plt


def draw_squares(ax, center, length):
    mid = length / 2
    x = np.array([[center[0] - mid, center[1] + mid], [center[0] + mid, center[1] + mid],
                 [center[0] + mid, center[1] - mid], [center[0] - mid, center[1] - mid],
                 [center[0] - mid, center[1] + mid]]) # Used to plot the 5 coordinates used to draw a square from center point
    ax.plot(x[:,0], x[:,1], color='k')

def draw_square_flower(ax, center, numTimes, length):
    mid = length / 2
    if numTimes > 0:
        draw_squares(ax, center, length)
        point1 = [center[0] - mid, center[1] + mid]
        point2 = [center[0] + mid, center[1] + mid]
        point3 = [center[0] + mid, center[1] - mid]
        point4 = [center[0] - mid, center[1] - mid]
        #creates new center points for squares to be drawn

        draw_square_flower(ax, point1, numTimes - 1, length / 2)
        draw_square_flower(ax, point2, numTimes - 1, length / 2)
        draw_square_flower(ax, point3, numTimes - 1, length / 2)
        draw_square_flower(ax, point4, numTimes - 1, length / 2)
        #draws eac hof the squares in the respective corner


size = 800

plt.close('all')
fig, ax = plt.subplots()
draw_square_flower(ax, [0, 0], 2, size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('square1.png')

plt.close("all")
fig, ax = plt.subplots()
draw_square_flower(ax, [0, 0], 3, size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares2.png')

plt.close("all")
fig, ax = plt.subplots()
draw_square_flower(ax,[0, 0], 4, size)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares3.png')
