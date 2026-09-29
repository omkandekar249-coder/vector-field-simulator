import numpy as np
from functions.parser import parse_function
from functions.plot import plot_vector_field

print("Vector Field Simulator")
print("Enter P(x, y) and Q(x, y) for the vector field F = <P, Q>")

P_input = input("P(x, y) = ")
Q_input = input("Q(x, y) = ")

P = parse_function(P_input)
Q = parse_function(Q_input)

xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
ymin = float(input("Enter ymin: "))
ymax = float(input("Enter ymax: "))

density = int(input("Enter density (20–40 recommended): "))

plot_vector_field(
    P,
    Q,
    x_range=(xmin, xmax),
    y_range=(ymin, ymax),
    density=density
)

