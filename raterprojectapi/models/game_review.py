from django.db import models
from .gamer import Gamer
from .game import Game

class GameReview(models.Model):
    
    description = models.CharField(max_length=200)
    user_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
