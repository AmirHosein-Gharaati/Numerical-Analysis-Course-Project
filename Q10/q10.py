import numpy as np
import matplotlib.pyplot as plt

def generate_zero_matrix():
    x_range, y_range = [0, 10], [0, 8]
    h = 0.01
    x_count, y_count = int(x_range[-1] // h), int(y_range[-1] // h)
    return x_count, y_count, np.zeros([x_count+1, y_count+1]), h


def fill_matrix():
    x_count, y_count, matrix, h = generate_zero_matrix()
    for x in range(x_count + 1):
        matrix[x,0], matrix[x,-1] = 6, 5 * x * h + 2
    for y in range(y_count + 1):
        matrix[0,y], matrix[-1,y] = y * h, 3*y*h

    for _ in range(1): # the more the better accurancy
        for i in range(1, x_count):
            for j in range(1, y_count):
                matrix[i,j] = (matrix[i-1,j] + matrix[i+1,j] + matrix[i,j+1] + matrix[i,j-1]) / 4

    x = range(x_count + 1)
    y = range(y_count + 1)
    x_range, y_range = np.meshgrid(x,y)
    return matrix, x_range, y_range, h


def draw_plot():
    matrix, x_range, y_range, h = fill_matrix()
    z_value = lambda mat, i, j: mat[i, j]

    x_axis, y_axis = x_range * h, y_range * h

    ax = plt.axes(projection= '3d')
    ax.get_figure().set_size_inches(12, 9)
    ax.plot_surface(
        x_axis,
        y_axis,
        z_value(matrix, x_range, y_range),
        cmap='inferno')

    plt.savefig('./Q10/plots/Q10')
    for angle in range(0, 360):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.001)

if __name__ == '__main__':
    draw_plot()
