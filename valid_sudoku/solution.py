from typing import List

class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        segments = self.get_boxes()
        segments.extend(self.get_rows())
        segments.extend(self.get_cols())
        for segment in segments:
            s = set()
            for box in segment:
                value = board[box[0]][box[1]]
                if value in s:
                    return False
                if value != ".":
                    s.add(value)
        return True

    def get_boxes(self) -> List[List[int]]:
        boxes = []
        for k in range(3):
            for l in range(3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append((i+3*k, j+3*l))
                boxes.append(box)
        return boxes
    
    def get_rows(self) -> List[List[int]]:
        rows = []
        for k in range(9):
            row = []
            for i in range(9):
                row.append((k, i))
            rows.append(row)
        return rows

    def get_cols(self) -> List[List[int]]:
        cols = []
        for k in range(9):
            col = []
            for i in range(9):
                col.append((i, k))
            cols.append(col)
        return cols
