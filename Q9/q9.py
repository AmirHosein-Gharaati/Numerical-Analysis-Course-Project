import math
import matplotlib.pyplot as plt


def RK4_method_solver(t, h, y, dy):
    func_calc = lambda t, y, dy:  pow(t, 2) * y- (4 * dy) + (pow(t, 4) * math.log(t))
    t_range, y_range, dy_range = [new_t + h for new_t in range(100)], list(), list()
    for _ in range(100):
        y_k= h * (dy + (h * func_calc(t + h/2, y+ (h * dy)/2, dy + (h * func_calc(t, y, dy))/2))/2)
        dy_k = h * func_calc(
            t + h/2,
            y+ (h * (dy + (h * func_calc(t, y, dy))/2))/2,
            dy + (h * func_calc(t + h/2,
            y+ (h * dy)/2,
            dy + (h * func_calc(t, y, dy))/2))/2
        )
        y_k_1= h * (dy + dy_k)
        dy_k_1 = h * func_calc(
                            t + h,
                            y+ y_k,
                            dy + dy_k
                        )
        t += h
        y += ((h * dy)+ 2 * (h * (dy + (h * func_calc(t, y, dy))/2))+ 2 * y_k+ y_k_1)/6
        dy += (
            (h * func_calc(t, y, dy)) + 2 * (h * func_calc(t + h/2, y+ (h * dy)/2, dy + (h * func_calc(t, y, dy))/2)) + 2 * dy_k + dy_k_1)/6
        y_range.append(y)
        dy_range.append(dy)
    return t_range, y_range, dy_range


def initial_values():
    h, t, y, dy = (8 - 2) / 100, 2, 1, 1
    return t, h, y, dy


def draw_plot():
    t_range, y_range, dy_range = RK4_method_solver(*initial_values())

    fig, axs = plt.subplots(1, 2)
    axs[0].plot(t_range, y_range)
    axs[0].set_title('y(t)')

    axs[1].plot(t_range, dy_range, 'tab:orange')
    axs[1].set_title('y`(t)')

    fig.set_size_inches(12, 9)
    fig.suptitle('Q9')
    plt.savefig('./Q9/plots/Q9.png')
    plt.show()


if __name__ == '__main__':
    draw_plot()
