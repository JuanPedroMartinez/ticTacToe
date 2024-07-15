from django.db import models


# Create your models here.
class Game(models.Model):
    GAME_STATUS = (('X', 'X'), ('O', 'O'), ('E', 'Empate'), ('J', 'Jugando'), ('T', 'Finalizado'))
    board = models.CharField(max_length=9, default='---------')
    next_turn = models.CharField(max_length=1, default='X')
    winner = models.CharField(max_length=1, default='')

    def __str__(self):
        return f"Game #{self.id}"



