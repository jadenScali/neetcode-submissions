class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        squares = [[] for _ in range(9)]

        for i in range(9):
            curr_row = []
            curr_col = []

            for j in range(9):
                curr_row.append(board[i][j])
                curr_col.append(board[j][i])
                squares[i//3 % 3 + 3*(j//3 % 3)].append(board[i][j])


            rows.append(curr_row)
            cols.append(curr_col)

        print(squares)
        sets = []
        sets.extend(rows)
        sets.extend(cols)
        sets.extend(squares)

        for s in sets:
            seen = {}
            for i in s:
                if i in seen and i != '.':
                    return False
                seen[i] = True
        
        return True
                
        