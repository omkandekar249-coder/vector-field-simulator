import numpy as np

def parse_function(user_input):
    allowed = {
        'np': np,
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'exp': np.exp,
        'sqrt': np.sqrt,
        'log': np.log,
        'abs': np.abs
    }

    def f(x, y):
        return eval(user_input, {"__builtins__": {}}, {**allowed, 'x': x, 'y': y})

    return f

