from typing import List

def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    flat = [num for row in mat for num in row]
    if len(flat) != r * c:
        return mat
    return [flat[i * c:(i + 1) * c] for i in range(r)]

print(matrixReshape([[1,2],[3,4]], 1, 4))
