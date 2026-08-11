import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        result = [[0] * c for _ in range(r)]

        for i in range(m):
            for j in range(n):
                index = i * n + j

                new_row = index // c
                new_col = index % c

                result[new_row][new_col] = mat[i][j]

        return result