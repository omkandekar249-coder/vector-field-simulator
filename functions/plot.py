import numpy as np
import matplotlib.pyplot as plt
from .vectorfield import compute_vector_field

def plot_vector_field(P, Q, x_range, y_range, density=20):
    x = np.linspace(*x_range, density)
    y = np.linspace(*y_range, density)
    X, Y = np.meshgrid(x, y)

    U, V = compute_vector_field(P, Q, X, Y)

    plt.figure(figsize=(8, 6))
    plt.quiver(X, Y, U, V, color='blue')

    plt.title("Vector Field Simulator")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
