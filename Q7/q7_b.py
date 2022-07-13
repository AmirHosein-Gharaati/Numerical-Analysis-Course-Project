import matplotlib.pyplot as plt


def generate_from_deta():
    with open("./Q7/deta.txt") as data_file:
        data = data_file.readlines()
        x_range = [ float(row.strip().split()[0]) for row in data ]
        y_range = [ float(row.strip().split()[1]) for row in data ]
    points_count = len(data)

    return x_range, y_range, points_count


def central_difference(x_range, y_range, from_i, to_i):
    d_x_range = x_range[from_i: to_i]
    d_y_range = [ (y_range[i+1] - y_range[i-1]) / (x_range[i+1]-x_range[i-1])
                    for i in range(from_i, to_i)
                ]

    return d_x_range, d_y_range

def draw_plot():
    x_range , y_range, points_count = generate_from_deta()
    d_x_range, d_y_range = central_difference(x_range, y_range, 1, points_count-1)

    print('checkout <./Q7/plots> path, the plot has been saved there.')
    plt.plot(d_x_range, d_y_range, 'orange')
    plt.axis([-11, 11, -350, 350])
    plt.title('Q7 - part b')
    plt.savefig('./Q7/plots/Q7_part_b.png')
    plt.show()


if __name__ == '__main__':
    draw_plot()
