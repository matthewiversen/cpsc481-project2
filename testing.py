board = [0, 5, 3, 1]

moves = []

for row in range(len(board)):
    for match_amount in range(1, board[row] + 1):
        moves.append((row, match_amount))

print(moves)