import matplotlib.pyplot as plt


def generate_from_deta():
    with open("./Q7/deta.txt") as data_file:
        data = data_file.readlines()
        x_range = [ float(row.strip().split()[0]) for row in data ]
        y_range = [ float(row.strip().split()[1]) for row in data ]
    points_count = len(data)

    return x_range, y_range, points_count


def second_derivative_central_difference():
    x_range, y_range, _ = generate_from_deta()
    h = x_range[1] - x_range[0]


    d2_x_range = x_range[5: 9992]
    d2_y_range = [ (y_range[i+1]-(2*y_range[i])+y_range[i-1])/(h**2) for i in range(5, 9992) ]

    print('checkout <./Q7/plots> path, the plot has been saved there.')
    plt.plot(d2_x_range, d2_y_range, 'orange')
    plt.axis([-11, 11, -30000, 1500])
    plt.title('Q7 - part c')
    plt.savefig('./Q7/plots/Q7_part_c.png')
    plt.show()


if __name__ == '__main__':
    second_derivative_central_difference()