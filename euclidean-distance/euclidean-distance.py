import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    sum = 0
    for i in range(0, len(x)):
        d = abs(x[i]-y[i])**2
        sum = sum + d
    return np.sqrt(sum)