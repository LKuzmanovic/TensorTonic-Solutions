import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    total = 0
    if (len(x) != len(y)):
        return 0
    for i in range(len(x)):
        total += x[i] * y[i]
    return float(total)