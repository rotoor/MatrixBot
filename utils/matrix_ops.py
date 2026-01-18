import numpy as np  # full ???


def parse_matrix(text: str) -> np.ndarray:
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except Exception as e:
        raise ValueError(f"Wrong matrix format: {e}")


def transpose(matrix: np.ndarray) -> np.ndarray:
    return matrix.T
