#A Program which generates a line of best fit in the form, y = mx + b, which minimizes y-value error for estimations
#based on data using linear regression

#limited as m is only in the range -10 to 10 in 0.1 steps, and b is in the range -20 to 20 in 0.1 steps,
#so accuracy is limited to 1 decimal place, also meaning data in the datapoints list should respect this limitation. :)

#DATA TO INSERT (x, y)
datapoints = [(0, 2), (1, 4), (2, 5), (3, 5), (4, 7), (5, 8)]

def get_y(m, b, x):
    return m * x + b
#print(get_y(1, 0, 7) == 7) prints true
#point is list x y [x, y]
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    return abs(get_y(m, b, x_point) - y_point) #make difference always positive
#^^ returns difference between y-values of y = mx + b line and the point we gave

def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m, b, point)
    return total_error
#print(calculate_all_error(1, 0, datapoints))

#finding m and b values to minimize error through trail and error
#list of m's from -10 to 10 in 0.1's
possible_ms = [m*0.1 for m in range(-100, 100)]
#list of b's from -20 to 20 in 0.1's
possible_bs = [b*0.1 for b in range(-200, 200)]

smallest_error = float('inf')
best_m = 0
best_b = 0

#iterate through m's and b's and calculate smallest error
for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            smallest_error = error
            best_m = m
            best_b = b
best_m = round(best_m, 1)
best_b = round(best_b, 1)
#print best m, b and smallest error
print('\n')
print('Best gradient is ' + str(best_m) + ' (1 d.p.)')
print('Best y-intercept is ' + str(best_b) + ' (1 d.p.)')
print('The smallest error is ' + str(round(smallest_error, 1)) + ' (1 d.p.)')
print('\n')
