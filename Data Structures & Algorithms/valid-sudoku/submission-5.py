class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_seen: dict[int, set[str]] = {}
        col_seen: dict[int, set[str]] = {}
        box_seen: dict[int, set[str]] = {}

        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val != '.':
                    row_seen.setdefault(row, set())
                    col_seen.setdefault(col, set())

                    r, c = row // 3, col // 3
                    box_id = r * 3 + c
                    box_seen.setdefault(box_id, set())

                    if val in row_seen[row]:
                        return False 
                    if val in col_seen[col]:
                        return False
                    if val in box_seen[box_id]:
                        return False
                    
                    row_seen[row].add(val)
                    col_seen[col].add(val)
                    box_seen[box_id].add(val)
    
        return True
