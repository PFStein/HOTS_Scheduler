from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from teams.models import Player,Role,Team

class IndexView(generic.ListView):
    template_name = 'teams/index.html'
    context_object_name = 'active_teams'

    def get_queryset(self):
        """Return all of the teams."""
        return Team.objects.all();

class TeamDetailView(generic.ListView):
    model = Team
    template_name = 'teams/team_details.html'
    
class PlayerDetailView(generic.ListView):
    model = Player
    template_name = 'teams/player_details.html'    
    
class CalendarView():
    

