from rest_framework.decorators import action
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game

class GameView(ViewSet):
    
    def retrieve(self, request, pk):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """_summary_

        Args:
            request (_type_): _description_
        """
        games = Game.objects.all()

        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class GameSerializer(serializers.ModelSerializer):
    """"JSON serializer for games"""
    class Meta:
        model = Game
        fields = ('id', 'title', 'designer','year', 'number_of_players', 'est_time_of_play', 'age_recommendation', 'user_id')
        depth = 1
