def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    seen = set()
    count = 0
    for r in range(0,9):
        for c in range(0,9):
            if board[r][c] == ".":
                continue
            if board[r][c] in seen:
                return False
            else:
                count+=1
                seen.add(board[r][c])
        seen = set()
    for r in range(0,9):
        for c in range(0,9):
            if board[c][r] == ".":
                continue
            if board[c][r] in seen:
                return False
            else:
                seen.add(board[c][r])
        seen = set()

    boxes = {}
    for r in range(0,9):
        for c in range(0,9):
            if board[r][c] == ".":
                continue
            box_id = (r//3,c//3)
            if box_id not in boxes:
                boxes[box_id] = []
            if board[r][c] in boxes[box_id]:
                return False
            boxes[box_id].append(board[r][c])
    
    return True

test = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(test))

test = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(test))