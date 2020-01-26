from django.urls import path

from event.views import (
    index, winner_list,add_players
)

app_name = 'event'

urlpatterns = [
    path('', index, name='index'),
    path('winner/', winner_list, name='winner'),
    path('add_players/', add_players, name='add_players'),

]
