class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                number = board[i][j]

                if not number.isdigit():
                    continue

                if number in rows[i]:
                    return False
                
                rows[i].add(number)

                if number in columns[j]:
                    return False

                columns[j].add(number)

                if number in squares[((i // 3) * 3 + (j // 3))]:
                    return False

                squares[((i // 3) * 3 + (j // 3))].add(number)

        return True

                
