import numpy as np


def generate_matrix(mean: float, st_dev: float, n: int) -> np.ndarray:
    return np.random.normal(mean, st_dev, (n, n))
