class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_seen: dict[int, list] = {}
        col_seen: dict[int, list] = {}
        box_seen: dict[int, list] = {}

        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val != '.':
                    row_seen.setdefault(row, []).append(val)
                    col_seen.setdefault(col, []).append(val)

                    r, c = row // 3, col // 3
                    box_id = r * 3 + c
                    box_seen.setdefault(box_id, []).append(val)
        
        for i in range(9):
            row_cond = len(row_seen.get(i, [])) != len(set(row_seen.get(i, [])))
            col_cond = len(col_seen.get(i, [])) != len(set(col_seen.get(i, [])))
            box_cond = len(box_seen.get(i, [])) != len(set(box_seen.get(i, [])))

           

            if row_cond or col_cond or box_cond:
                return False
            
        return True
