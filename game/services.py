from game.models import Game

def getGamesForUser(user):
    if user.is_authenticated:
        return Game.objects.filter(user=user)
    return Game.objects.none()
