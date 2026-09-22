import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)
    if mag_a == 0 or mag_b == 0:
        return 0.0
    similarity = np.dot(a, b)/(np.linalg.norm(a) * np.linalg.norm(b))
    return float(similarity)