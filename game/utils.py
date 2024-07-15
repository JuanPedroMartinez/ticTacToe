from game.models import Game


def is_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw(board):
    # Función para verificar si es un empate
    return '-' not in board and not is_winner(board, 'X') and not is_winner(board, 'O')


def count_wins():
    print(Game.objects)
    wins = {
        'win_X': Game.objects.filter(winner='X').count(),
        'win_O': Game.objects.filter(winner='O').count(),
        'draw_E': Game.objects.filter(winner='E').count()
    }
    return wins
