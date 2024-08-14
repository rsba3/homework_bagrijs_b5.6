board = 3

field = ['-' for i in range(9)]

def create_field():
    print(' ', 1, 2, 3)
    for i in range(board):
        start = i * board
        print(i + 1, field[start], field[start + 1], field[start + 2])

def make_move(player, position):
    if field[position - 1] == '-':
        field[position - 1] = player
        return True
    else:
        print('Cell taken! Try another move')
        return False
def check_win():
    win_positions = [
        (0, 1, 2), (0, 4, 8), (6, 7, 8),
        (0, 3, 6), (2, 4, 6), (2, 5, 8),
        (1, 4, 7), (3, 4, 5)
    ]
    for pos in win_positions:
        if field[pos[0]] == field[pos[1]] == field[pos[2]] and field[pos[0]] != '-':
            return True
    return False

def start_game():
    current_move = 'x'
    create_field()

    while True:
        value = input(f'Move make {current_move} (1-9):')
        if not value.isdigit() or not (1 <= int(value) <= 9):
            print('Choose value from 1 to 9')
            continue

        value = int(value)

        if make_move(current_move, value):
            create_field()
            if check_win():
                print(f'Player {current_move} win')
                break
            if '-' not in field:
                print("Draw")
                break
            current_move = '0' if current_move == 'x' else 'x'
start_game()