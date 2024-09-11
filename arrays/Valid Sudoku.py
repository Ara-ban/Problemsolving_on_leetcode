from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ligns, columns, squares = {}, {}, {}
        
        for i in range(9):
            ligns[i] = set()
            columns[i] = set()
            squares[i] = set()
        
        for i in range(9):
            for j in range(9):
                a = board[i][j]
                if a != ".":
                    square_index = (i // 3) * 3 + (j // 3)
                    if a in ligns[i] or a in columns[j] or a in squares[square_index]:
                        return False
                    ligns[i].add(a)
                    columns[j].add(a)
                    squares[square_index].add(a)
        
        return True
