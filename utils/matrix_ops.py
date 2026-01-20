import numpy as np


def parse_matrix(text: str) -> np.ndarray:
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(float, row.split())) for row in rows]
        return np.array(matrix)
    except Exception as e:
        raise ValueError(f"Wrong matrix format: {e}")


def transpose(matrix: np.ndarray) -> np.ndarray:
    return matrix.T


def determinant(matrix: np.ndarray) -> float:
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")
    return float(np.linalg.det(matrix))


def add(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    if matrix1.shape != matrix2.shape:
        raise ValueError("Matrices must be...")
    return matrix1 + matrix2


def multiply(matrix1: np.ndarray, matrix2: np.ndarray) -> np.ndarray:
    if matrix1.shape[1] != matrix2.shape[0]:
        raise ValueError("Matrices must be...")
    return matrix1 @ matrix2

def inverse(matrix: np.ndarray) -> np.ndarray:
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square")
    if np.isclose(np.linalg.det(matrix), 0):
        raise ValueError("Determinant is 0.")
    return np.linalg.inv(matrix)