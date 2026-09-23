import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    # sum = 0
    # for i in range(0, len(x)):
    #    sum += abs(x[i]-y[i])
    # return float(sum)
    z = np.array(x)-np.array(y)
    return np.linalg.norm(z, ord=1)