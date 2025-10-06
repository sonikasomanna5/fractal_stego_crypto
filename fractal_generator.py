import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot(width=800, height=800, zoom=1, filename="assets/output/fractal.png"):
    x = np.linspace(-2.5 / zoom, 1.5 / zoom, width)
    y = np.linspace(-2 / zoom, 2 / zoom, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C)
    img = np.zeros(C.shape, dtype=int)

    for i in range(256):
        Z = Z**2 + C
        mask = (np.abs(Z) < 4) & (img == 0)
        img[mask] = i

    plt.imshow(img, cmap='inferno', extent=(-2, 1, -1.5, 1.5))
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    return filename
