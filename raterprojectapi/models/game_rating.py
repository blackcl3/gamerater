from django.db import models
from .game import Game
from .gamer import Gamer

class GameRating(models.Model):
    
    rating = models.IntegerField()
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)
