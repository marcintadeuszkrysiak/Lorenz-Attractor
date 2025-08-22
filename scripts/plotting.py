import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_3d(x, y, z, title='Lorenz Attractor', ax=None, c=None, lw=0.5):
    if ax is None:
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection='3d')
    if c is None:
        ax.plot(x, y, z, lw=lw)
    else:
        sc = ax.scatter(x, y, z, c=c, s=0.2, cmap='viridis')
    ax.set_title(title)
    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    return ax

def plot_projections(x, y, z):
    fig, axs = plt.subplots(1, 3, figsize=(12, 3.5))
    axs[0].plot(x, y); axs[0].set_xlabel('x'); axs[0].set_ylabel('y'); axs[0].set_title('x-y')
    axs[1].plot(x, z); axs[1].set_xlabel('x'); axs[1].set_ylabel('z'); axs[1].set_title('x-z')
    axs[2].plot(y, z); axs[2].set_xlabel('y'); axs[2].set_ylabel('z'); axs[2].set_title('y-z')
    fig.tight_layout()
    return axs

def plot_time_series(t, x, y, z):
    fig, axs = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
    axs[0].plot(t, x); axs[0].set_ylabel('x(t)')
    axs[1].plot(t, y); axs[1].set_ylabel('y(t)')
    axs[2].plot(t, z); axs[2].set_ylabel('z(t)'); axs[2].set_xlabel('t')
    fig.tight_layout()
    return axs