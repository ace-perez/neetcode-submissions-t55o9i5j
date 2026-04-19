class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        memo = [[0] * cols for _ in range(rows)]

        import sys
        sys.setrecursionlimit(20000)

        def dfs(i: int, j: int) -> int:
            if memo[i][j] != 0:
                return memo[i][j]

            best = 1

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[i][j]:
                    best = max(best, 1 + dfs(nr, nc))

            memo[i][j] = best
            return best

        max_length = 0
        for i in range(rows):
            for j in range(cols):
                max_length = max(max_length, dfs(i, j))

        return max_length