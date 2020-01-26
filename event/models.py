from django.db import models


class Player(models.Model):
    players = models.CharField('Player', max_length=100)

    def __str__(self):
        return self.players


class WinnerPlayer(models.Model):
    player_a = models.ForeignKey(Player, related_name='player_a', on_delete=models.CASCADE)
    player_b = models.ForeignKey(Player, related_name='player_b', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
