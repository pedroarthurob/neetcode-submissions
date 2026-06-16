class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            row_set = set()
            for column in range(9):
                number = board[row][column]
                if number.isdigit() and number in row_set:
                    return False
                
                if number.isdigit():
                    row_set.add(number)

        for column in range(9):
            column_set = set()
            for row in range(9):
                number = board[row][column]
                if number.isdigit() and number in column_set:
                    return False

                if number.isdigit():
                    column_set.add(number)

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                # Here we are at the top left of every square
                square_set = set()
                for row in range(i, i + 3):
                    for column in range(j, j + 3):
                        number = board[row][column]
                        if number.isdigit() and number in square_set:
                            return False

                        if number.isdigit():
                            square_set.add(number)

        return True

                
