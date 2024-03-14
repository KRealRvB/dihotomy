import math

start = 0
end = 1
epsilon = 0.1
D = epsilon / 2
epsilon_new = epsilon * 2

def function_of_x(x):
    return x**3 - math.sin(x)

while epsilon_new > epsilon:
    x1 = (start + end - D) / 2
    x2 = (start + end + D) / 2

    if function_of_x(x1) <= function_of_x(x2):
        end = x2
    else:
        start = x1

    epsilon_new = (end - start) / 2

x_best = (start + end) / 2
print(function_of_x(x_best), x_best)