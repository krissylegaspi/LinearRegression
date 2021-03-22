y = m*x + b

def get_y(m, b, x):
    y = m*x + b
    return y

def calculate_error(m, b, point):
    x_point, y_point = point
    y = m*x_point + b
    distance = abs(y - y_point)
    return distance

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def calculate_all_error(m, b, points):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error

possible_m_values = [m * 0.1 for m in range(-100, 101)]
possible_b_values = [b * 0.1 for b in range(-200, 201)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("infinity")
best_m = 0
best_b = 0

for m in possible_m_values:
    for b in possible_b_values:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

print(best_m, best_b, smallest_error)

get_y(0.3, 1.7, 6)