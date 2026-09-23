import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    z = np.array(x)-np.array(y)
    return np.linalg.norm(z)