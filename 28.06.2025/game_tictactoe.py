board = [' ' for _ in range(9)]
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6: print("-" * 9)
def check_win(player):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)
current = 'X'
while True:
    print_board()
    pos = int(input(f"Player {current}, enter position (1-9): ")) - 1
    if 0 <= pos < 9 and board[pos] == ' ':
        board[pos] = current
        if check_win(current):
            print_board()
            print(f"Player {current} wins!")
            break
        if ' ' not in board:
            print_board()
            print("It's a tie!")
            break
        current = 'O' if current == 'X' else 'X'