from django.contrib import messages
from django.db.models import Count, Max
from django.shortcuts import render, redirect

from event.models import Player, WinnerPlayer


def index(request):
    player = Player.objects.all().order_by('-id')
    current_standing = WinnerPlayer.objects.values('winner__players').annotate(
        winner_count=Count('winner')).order_by('-winner_count')[:5]

    if request.method == 'POST':
        player_name_a = request.POST['p1']
        player_name_b = request.POST['p2']
        winner = request.POST['winner']
        WinnerPlayer.objects.create(
            player_a=Player.objects.filter(id=player_name_a).first(),
            player_b=Player.objects.filter(id=player_name_b).first(),
            winner=Player.objects.filter(id=winner).first(),
        )
        messages.success(request, 'Winner Added Successfully')
        return redirect('race:index')
    return render(request, 'event/index.html', {'player': player, 'st': current_standing})


def winner_list(request):
    winner = WinnerPlayer.objects.all().order_by('-id')

    return render(request, 'event/winner.html',
                  {'winner': winner}
                  )


def add_players(request):
    if request.method == 'POST':
        players = request.POST['add_player']
        Player.objects.create(
            players=players,
        )
        messages.success(request, 'Player Added Successfully!')
        return redirect('race:add_players')
    return render(request, 'event/add_player.html')
