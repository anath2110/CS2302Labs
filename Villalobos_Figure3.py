'''
    Code created and Modified by: Ismael Villalobos
    Skeleton code provide by: Olac Fuentes
    Date:2/12/19
    Lab1
'''
import numpy as np
import matplotlib.pyplot as plt


def draw_tree(ax, line, x, y, n):
    if n > 0:
        # Builds Branches
        left = [line[0] - x, line[1] - y]  # left branch
        right = [line[0] + x, line[1] - y]  # right branch

        ax.plot([line[0], left[0]], [line[1], left[1]],  # left branch
                [line[0], right[0]], [line[1], right[1]], linewidth=1,color='k')  # right branch

        # Recursive Calls for branches
        draw_tree(ax, left, x / 2, y*0.9, n - 1)  # Left branches
        draw_tree(ax, right, x / 2, y*0.9, n - 1)  # Right branches


# Draw uu = 100
line = np.array([0, 0])
x = 50
y = 50

# First
plt.close("all")
fig, ax = plt.subplots()
draw_tree(ax, line, x, y, 3)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('tree1.png')

# Second
plt.close("all")
fig, ax = plt.subplots()
draw_tree(ax, line, x, y, 4)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('tree2.png')

# Third
plt.close("all")
fig, ax = plt.subplots()
draw_tree(ax, line, x, y, 6)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('tree3.png')
