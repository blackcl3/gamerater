from django.db import models
from .gamer import Gamer

class Game(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    designer = models.CharField(max_length=100)
    year = models.DateField()
    number_of_players = models.IntegerField()
    est_time_of_play = models.IntegerField()
    age_recommendation = models.IntegerField()
    user_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)
