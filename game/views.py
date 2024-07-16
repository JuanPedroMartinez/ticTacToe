from venv import logger

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Game
from .services import getGamesForUser
from .utils import is_winner, is_draw, count_wins

# Create your views here.

def homePage(request):
    userGames = getGamesForUser(request.user)
    wins = count_wins(request.user)
    return render(request, 'game/home.html', {'games':userGames, 'wins':wins})
def new_game(request):
    if request.method == 'POST':
        game = Game.objects.create(user=request.user)
        return redirect('board', game_id=game.id)
    return render(request, 'game/home.html')

def play(request, game_id):
    game = get_object_or_404(Game, id=game_id) #recuperamos el juego y devolvemos 404 si no existe.
    if request.method == 'POST':
        position = int(request.POST.get('position'))
        board = list(game.board)
        if board[position] == '-':
            board[position] = game.next_turn
            game.board = ''.join(board)

            game.next_turn = 'O' if game.next_turn == 'X' else 'X'
            game.save()
            return redirect('board', game_id=game.id)
        else:
            return JsonResponse({'error': 'Invalid move'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def board(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if is_winner(game.board ):  # Comprobamos si se ha producido la victoria
        game.winner = game.next_turn
        game.next_turn = 'T'
        game.save()
        return render(request, 'game/game_finished.html', {'game': game})
    elif is_draw(game.board):  # Comprobamos si se ha producido un empate
        game.next_turn = 'E'
        game.save()
        return render(request, 'game/game_finished.html', {'game': game})

    return render(request, 'game/board.html', {'game': game})

def game_finished(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'game/game_finished.html', {'game': game})

