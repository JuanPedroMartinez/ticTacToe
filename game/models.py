from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Game(models.Model):
    GAME_STATUS = (('X', 'player X'), ('O', 'player O'), ('E', 'Draw'), ('P', 'Playing'), ('T', 'Finished'))
    board = models.CharField(max_length=9, default='---------')
    next_turn = models.CharField(max_length=1, default='X')
    winner = models.CharField(max_length=1, default='')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return f"Game #{self.id}"



