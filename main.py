import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return np.array([int(hex_color[i:i+2], 16) for i in (0, 2, 4)])

def lighten_color(color, factor=0.5):
    white = np.array([1.0, 1.0, 1.0])
    return color + (white - color) * factor

file_path = 'pic3.png'
image = cv2.imread(file_path)
height, width, _ = image.shape

blue, green, red = cv2.split(image)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y = np.meshgrid(range(width), range(height))

start_color_blue = hex_to_rgb('#0000FF') / 255.0
middle_color_green = hex_to_rgb('#00FF00') / 255.0
end_color_red = hex_to_rgb('#FF0000') / 255.0
N = 20

colors_blue_to_green = np.linspace(start_color_blue, middle_color_green, N//2)
colors_green_to_red = np.linspace(middle_color_green, end_color_red, N//2)

colors = np.vstack((colors_blue_to_green, colors_green_to_red))
#lightened_colors = np.array([lighten_color(c, factor=0.7) for c in colors])
lightened_colors = colors

for i, c in enumerate(lightened_colors):
    pos = i * (-1)
    fc = np.dstack([c[0] * blue, c[1] * green, c[2] * red]) / 255.0
    ax.plot_surface(x+i*3, y+i, np.full_like(x, pos), rstride=1, cstride=1, facecolors=fc, shade=False)

ax.view_init(elev=110, azim=-90)
ax.set_axis_off()

plt.savefig('cube.png', transparent=True)
#plt.show()
