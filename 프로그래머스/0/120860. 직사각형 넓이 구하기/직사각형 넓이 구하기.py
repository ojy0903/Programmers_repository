def solution(dots):

    x_max, x_min = dots[0][0], dots[0][0]
    y_max, y_min = dots[0][1], dots[0][1]

    for dot in dots:
        x_point, y_point = dot[0], dot[1]
        if x_point > x_max:
            x_max = x_point
        elif x_point < x_min:
            x_min = x_point

        if y_point > y_max:
            y_max = y_point
        elif y_point < y_min:
            y_min = y_point

    width = x_max - x_min
    height = y_max - y_min

    answer = width * height

    return answer