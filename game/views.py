from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from .utils import is_winner, is_draw, count_wins


# Create your views here.

def new_game(request):
    if request.method == 'POST':
        game = Game.objects.create()
        return redirect('board', game_id=game.id)
    return render(request, 'game/new_game.html')

def play(request, game_id):
    game = get_object_or_404(Game, id=game_id) #recuperamos el juego y devolvemos 404 si no existe.
    if request.method == 'POST':
        position = int(request.POST.get('position'))
        board = list(game.board)
        if board[position] == '-':
            board[position] = game.next_turn
            game.board = ''.join(board)
            game.save()
            if is_winner(game.board, game.next_turn): # Comprobamos si se ha producido la victoria
                game.winner = game.next_turn
                game.next_turn = 'T'
                game.save()
                return render(request, 'game/game_finished.html', {'game': game})
            elif is_draw(game.board):               # Comprobamos si se ha producido un empate
                game.next_turn = 'E'
                game.save()
                return render(request, 'game/game_finished.html', {'game': game})

            else:
                game.next_turn = 'O' if game.next_turn == 'X' else 'X'
                game.save()
                return render(request, 'game/board.html', {'game': game})
        else:
            return JsonResponse({'error': 'Invalid move'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def board(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game/board.html', {'game': game})

def game_finished(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game/game_finished.html', {'game': game})

def score_table(request):
    wins = count_wins()
    print(wins)
    return render(request, 'game/score_table.html', {'wins': wins})
