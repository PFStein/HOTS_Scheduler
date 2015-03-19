from django.views import generic
from django.views.generic import TemplateView

from teams.models import Player,Role,Team,Event,Registrations
    
class HomeView(TemplateView):
    template_name = "home.html"
    
class AboutView(TemplateView):
    template_name = "about.html"
    
class Calendar(TemplateView):
    template_name = "teams/calendar"
    
class TeamIndexView(generic.ListView):
    template_name = 'teams/team_index.html'
    context_object_name = 'active_teams'

    def get_queryset(self):
        """Return all of the teams."""
        return Team.objects.all();
    
class PlayerIndexView(generic.ListView):
    template_name = 'teams/player_index.html'
    context_object_name = 'active_players'

    def get_queryset(self):
        """Return all of the teams."""
        return Player.objects.all();

class TeamDetailView(generic.ListView):
    model = Team
    template_name = 'teams/team_details.html'
    
class PlayerDetailView(generic.ListView):
    model = Player
    template_name = 'teams/player_details.html'    
    

