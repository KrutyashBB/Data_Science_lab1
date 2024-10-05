import numpy as np
import matplotlib.pyplot as plt


def draw_rectangle(a, b, m, n, rectangle_color, background_color):
    image = np.zeros((m, n, 3), dtype=np.uint8)
    image[:] = background_color

    start_x = (n - a) // 2
    start_y = (m - b) // 2
    image[start_y:start_y + b, start_x:start_x + a] = rectangle_color

    plt.imshow(image)
    plt.axis('off')
    plt.show()


def draw_ellipse(a, b, m, n, ellipse_color, background_color):
    image = np.zeros((m, n, 3), dtype=np.uint8)
    image[:] = background_color

    y, x = np.ogrid[:m, :n]
    center_x, center_y = n // 2, m // 2
    mask = ((x - center_x) ** 2) / (a ** 2) + ((y - center_y) ** 2) / (b ** 2) <= 1
    image[mask] = ellipse_color

    plt.imshow(image)
    plt.axis('off')
    plt.show()


draw_rectangle(500, 100, 500, 200, (0, 0, 0), (255, 255, 255))
draw_ellipse(200, 100, 800, 400, (0, 0, 0), (255, 255, 255))
