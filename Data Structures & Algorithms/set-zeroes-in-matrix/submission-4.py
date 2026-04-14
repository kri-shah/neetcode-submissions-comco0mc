class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_zero = False
        first_col_zero = False
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for c in range(COLS):
            if matrix[0][c] == 0:
                first_row_zero = True

        for r in range(ROWS):
            if matrix[r][0] == 0:
                first_col_zero = True

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, ROWS):
            if matrix[r][0] == 0:
                for c in range(1, COLS):
                    matrix[r][c] = 0

        for c in range(1, COLS):
            if matrix[0][c] == 0:
                for r in range(1, ROWS):
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0