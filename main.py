import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp

# Constants
inner_angular_velocity = 1.0  # Rotational speed of the inner rod
x = sp.pi  # Exact value of π

# Function to calculate the position of the end of the outer rod
def calculate_position(theta):
    z = sp.exp(theta * 1j) + sp.exp(x * theta * 1j)
    return z.as_real_imag()

# Create the figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_axis_off()
# Hide the graph grid
ax.grid(False)

# Initialize the lines with improved styling
inner_rod, = ax.plot([], [], 'black', linewidth=1, marker='o', markersize=6, markeredgecolor='black', markerfacecolor='black')
outer_rod, = ax.plot([], [], 'black', linewidth=1, marker='o', markersize=6, markeredgecolor='black', markerfacecolor='black')
path, = ax.plot([], [], 'black', linewidth=1)

# Initialize points to trace the path
path_x = []
path_y = []

# Function to initialize the animation
def init():
    inner_rod.set_data([], [])
    outer_rod.set_data([], [])
    path.set_data([], [])
    path_x.clear()
    path_y.clear()
    return inner_rod, outer_rod, path

# Function to update the animation
def update(frame):
    theta = inner_angular_velocity * frame
    inner_x, inner_y = calculate_position(theta)
    outer_x, outer_y = calculate_position(theta * x)
    
    path_x.append(outer_x)
    path_y.append(outer_y)
    
    path.set_data(path_x, path_y)
    inner_rod.set_data([0, inner_x], [0, inner_y])
    outer_rod.set_data([inner_x, outer_x], [inner_y, outer_y])
    
    return inner_rod, outer_rod, path

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 100, 5000), init_func=init, blit=True)

# Function to handle mouse scroll for smooth zooming with the canvas following the pointer
def on_scroll(event):
    axtemp = event.inaxes
    x_min, x_max = axtemp.get_xlim()
    y_min, y_max = axtemp.get_ylim()
    x_scale = (x_max - x_min) / 10
    y_scale = (y_max - y_min) / 10

    if event.button == 'up':
        x_center, y_center = event.xdata, event.ydata
        axtemp.set_xlim(x_min + x_scale, x_max - x_scale)
        axtemp.set_ylim(y_min + y_scale, y_max - y_scale)
    elif event.button == 'down':
        x_center, y_center = event.xdata, event.ydata
        axtemp.set_xlim(x_min - x_scale, x_max + x_scale)
        axtemp.set_ylim(y_min - y_scale, y_max + y_scale)
    plt.draw()

# Connect the scroll event to the figure
fig.canvas.mpl_connect('scroll_event', on_scroll)

plt.show()
