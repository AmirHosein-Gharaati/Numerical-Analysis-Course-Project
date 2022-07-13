def generate_from_deta():
    with open("./Q7/deta.txt") as data_file:
        data = data_file.readlines()
        x_range = [ float(row.strip().split()[0]) for row in data ]
        y_range = [ float(row.strip().split()[1]) for row in data ]
    points_count = len(data)

    return x_range, y_range, points_count


def simpson_integral_calc():
    x_range, y_range, points_count = generate_from_deta()
    h = x_range[1] - x_range[0]

    result, i = 0, 1
    for y in y_range[1:-1] :
        if i%2 == 0:
            result += y * 2
        else:
            result += y * 4
        i += 1

    result = round((h/3)*((y_range[0]+y_range[-1]) + result), 6)

    print('\n\n-------------------------------------------------------------------------------------------')
    print(f'h = {h}, number of points = {points_count}')
    print(f'result of integral using simpson method with accurancy of 6 float points = {result}')
    print('-------------------------------------------------------------------------------------------\n\n')


if __name__ == '__main__':
    simpson_integral_calc()
