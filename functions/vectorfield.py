import numpy as np

def compute_vector_field(P, Q, X, Y):
    U = P(X, Y)
    V = Q(X, Y)
    return U, V
