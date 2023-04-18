'''
Created on 18 avr. 2023

@author: Utilisateur
'''
import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
L = 10
T = 5
dt = 0.1

# Define the initial concentration function
def c0(x):
    return (1 - np.abs(x-1)) * ((x >= 0) & (x <= 2))

# Define the transport equation without diffusion
def transport_equation(u, c, x, t):
    return -u * np.gradient(c, x)

# Create the figure and axis objects
fig, ax = plt.subplots()

# Set the x and y limits of the plot
ax.set_xlim(-L, L)
ax.set_ylim(0, 1)

# Plot the initial concentration function
x = np.linspace(-L, L, 1000)
y = c0(x)
line, = ax.plot(x, y)

# Define the update function for the animation
def update(i):
    # Calculate the current time
    t = i * dt

    # Calculate the current concentration function
    x = np.linspace(-L, L, 1000)
    y = c0(x - u * t)

    # Update the plot
    line.set_data(x, y)
    ax.set_title('t = {:.1f}'.format(t))

# Create the animation object
u = 1
ani = FuncAnimation(fig, update, frames=range(int(T/dt)), interval=50)

# Show the animation
plt.show()
