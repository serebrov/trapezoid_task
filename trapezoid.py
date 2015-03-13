import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math

top = 4
bottom = 10
height = 5
diff = 0.02

fig = plt.figure(figsize=(bottom+2, height+2))
ax = fig.add_axes([0, 0, 1, 1], xlim=(-diff, bottom+2+diff), ylim=(-diff, top+2+diff),
                  xticks=range(bottom), yticks=range(top), aspect='equal', frameon=False)
ax.grid(True)

def get_trapezoid(angle):
    rad = math.pi * angle / 180.0
    topx = height * math.cos(rad)
    diag_points = [0, topx+top], [0, height]
    return np.array([[0, 0], [topx, height], [topx + top, height], [bottom, 0]]), diag_points

points, diag_pts = get_trapezoid(90)
poly = plt.Polygon(points, fc='g', ec='k', alpha=.5)
trap = ax.add_patch(poly)
median, = ax.plot([0, bottom], [height / 2.0, height / 2.0])
diag, = ax.plot([0, bottom], [0, height])

points = []
for angle in range(90, 0, -5):
    pts, diag_pts = get_trapezoid(angle)
    points.append((pts, diag_pts))

angle = 90
step = 5
num_steps = 90 / step
def animate(nframe):
    global angle, step
    angle = 90 - step * (nframe % num_steps)
    pts, diag_pts = get_trapezoid(angle)
    trap.set_xy(pts)
    diag.set_data(*diag_pts)

anim = animation.FuncAnimation(fig, animate, num_steps, interval=500)
plt.show()
