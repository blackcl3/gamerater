from django.db import models
from .game import Game
from .gamer import Gamer

class GameImage(models.Model):
    
    url = models.CharField(max_length=50)
    label = models.CharField(max_length=200)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    
