from django.contrib import admin

from event.models import Player, WinnerPlayer


@admin.register(Player)
class TradeMarkModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'players')
    list_filter = ('players',)


@admin.register(WinnerPlayer)
class TradeMarkModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'winner')
    readonly_fields = ('player_a', 'player_b', 'winner')
