from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        I want to store each column, row and subgrids in an arry of sets which I will
        use to compare inside those sets if it exist or not. If it exists then
        return False, this will complete and the end will return True
        """

        col_sets = [set() for _ in range(9)]
        row_sets = [set() for _ in range(9)]
        subgrids = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == '.':
                    continue
                
                current_subgrid = (i//3,j//3)
                if value in col_sets[i] or value in row_sets[j] or value in subgrids[current_subgrid]:
                    return False
                
                col_sets[i].add(value)
                row_sets[j].add(value)
                subgrids[current_subgrid].add(value)

        return True