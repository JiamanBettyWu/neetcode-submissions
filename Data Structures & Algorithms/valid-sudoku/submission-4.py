class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_seen: dict[int, list] = {}
        col_seen: dict[int, list] = {}
        box_seen: dict[int, list] = {}

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

            
        
        # for i in range(9):
        #     row_cond = len(row_seen.get(i, [])) != len(set(row_seen.get(i, [])))
        #     col_cond = len(col_seen.get(i, [])) != len(set(col_seen.get(i, [])))
        #     box_cond = len(box_seen.get(i, [])) != len(set(box_seen.get(i, [])))

        #     if row_cond or col_cond or box_cond:
        #         return False
            
        return True
