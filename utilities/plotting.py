import os
import matplotlib.pyplot as plt
import numpy as np

BASE_PLOTTING_PATH = 'images'

def plot(y, x, description: str, clear=True):
    xpoints = np.array(x)
    ypoints = np.array(y)
    if clear:
        plt.clf()
    plt.plot(xpoints, ypoints, 'o')
    plt.savefig(os.path.join(BASE_PLOTTING_PATH, description + '.png'))
