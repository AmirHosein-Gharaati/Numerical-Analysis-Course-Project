import numpy
import matplotlib.pyplot as plt
import warnings


def d_solver(args: list):
    iL1, iL2, vC1, vC2 = args

    es = 20
    R1, R2, R3, R4, R5 = 2 * pow(10, 3), 5 * pow(10, 3), 2 * pow(10, 3), 3* pow(10, 3), 2* pow(10, 3)
    C1, C2, L1, L2 = 50 * pow(10, -6), 100 * pow(10, -6), 50 * pow(10, -6), 10 * pow(10, -6)

    # calculate equivalent resistance
    R3_R4 = (R3*R4) / (R3+R4)
    eq_R = R5 + R3_R4

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        d_vC1 = iL1 / C1
        d_vC2 = (iL1 / C2) + (iL2 / C2)
        d_iL1 = (1/L1) * (R4*es) / (R3+R4) - (vC1/L1) - (vC2/L1) - iL1*((R1 + eq_R) / L1) -((iL2*eq_R) / L1) 
        d_iL2 = (1/L2) * (R4*es) / (R3+R4) - (vC2/L2) - ( (iL1*eq_R) / L2 ) -( iL2* (R2 + eq_R) ) / L2

    return d_iL1, d_iL2, d_vC1, d_vC2


def euler_solver():
    # range is [0, 7] with h = 0.01
    h = 0.01
    x_range = numpy.arange(0, 7.01, h)

    initial_x_range = numpy.array([0,0,0,0])
    x_d_array = []
    for _ in x_range:
        x_d_array.append(initial_x_range)
        d_res = numpy.array(d_solver(initial_x_range))
        y = initial_x_range + h * d_res
        initial_x_range = initial_x_range + h * (
            numpy.array(d_solver(initial_x_range)) + numpy.array(d_solver(y))) / 2

    iL1, iL2 = [ x[0] for x in x_d_array ], [ x[1] for x in x_d_array ]
    vC1, vC2 = [ x[2] for x in x_d_array ], [ x[3] for x in x_d_array ]
    return iL1, iL2, vC1, vC2


def draw_plot():
    iL1, iL2, vC1, vC2 = euler_solver()
    h = 0.01
    x_range = numpy.arange(0, 7.01, h)

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(x_range, vC1)
    axs[0, 0].set_title('vC1')

    axs[0, 1].plot(x_range, vC2, 'tab:orange')
    axs[0, 1].set_title('vC2')

    axs[1, 0].plot(x_range, iL1, 'tab:green')
    axs[1, 0].set_title('iL1')

    axs[1, 1].plot(x_range, iL2, 'tab:red')
    axs[1, 1].set_title('iL2')

    fig.set_size_inches(12, 9)
    fig.suptitle('Q8')
    plt.savefig('./Q8/plots/Q8.png')
    plt.show()


if __name__ == '__main__':
    draw_plot()