import numpy as np
import matplotlib.pyplot as plt

def plot_horizontal_subplots():
    # Plots two subplots side-by-side.
    # Left subplot: h(x) = cos(x)
    # Right subplot: k(x) = sin(x)
    
    x_values = np.linspace(0, 2 * np.pi, 100)
    h_values = np.cos(x_values)
    k_values = np.sin(x_values)
    
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.plot(x_values, h_values, color='blue', linestyle='-', label='h(x) = cos(x)')
    plt.xlabel('x')
    plt.ylabel('h(x)')
    plt.title('Plot of h(x) = cos(x)')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(x_values, k_values, color='green', linestyle='--', label='k(x) = sin(x)')
    plt.xlabel('x')
    plt.ylabel('k(x)')
    plt.title('Plot of k(x) = sin(x)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def plot_vertical_subplots():
    # Plots two subplots on top of each other.
    # Top subplot: h(x) = cos(x)
    # Bottom subplot: k(x) = sin(x)
    
    x_values = np.linspace(0, 2 * np.pi, 100)
    h_values = np.cos(x_values)
    k_values = np.sin(x_values)
    plt.figure(figsize=(10, 12))
    plt.subplot(2, 1, 1)
    plt.plot(x_values, h_values, color='blue', linestyle='-', label='h(x) = cos(x)')
    plt.xlabel('x')
    plt.ylabel('h(x)')
    plt.title('Plot of h(x) = cos(x)')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(x_values, k_values, color='green', linestyle='--', label='k(x) = sin(x)')
    plt.xlabel('x')
    plt.ylabel('k(x)')
    plt.title('Plot of k(x) = sin(x)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_horizontal_subplots()
    plot_vertical_subplots()
