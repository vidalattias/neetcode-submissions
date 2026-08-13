class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(l: List[str]):
            seen = {str(i):False for i in range(1,10)}
            for x in l:
                if x == '.':
                    continue
                if seen[x]:
                    return False
                seen[x] = True
            return True

        def return_rows(board) -> List[List[str]]:
            return board

        def return_cols(board):
            cols = []
            for i in range(9):
                new_col = [board[j][i] for j in range(9)]
                cols.append(new_col)
            return cols

        def return_boxes(board):
            boxes = []
            for i in range(3):
                for j in range(3):
                    box = board[3*i][3*j:3*j+3] + board[3*i+1][3*j:3*j+3] + board[3*i+2][3*j:3*j+3]
                    boxes.append(box)
            return boxes

        to_check = return_rows(board) +  return_cols(board) + return_boxes(board)
        res = [check(x) for x in to_check]
        return False not in res