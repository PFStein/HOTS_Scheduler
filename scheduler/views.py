from django.views import generic
from django.views.generic import TemplateView

from scheduler.models import Player,Role,Team,Event,Registration
    
class HomeView(TemplateView):
    template_name = "home.html"
    
class AboutView(TemplateView):
    template_name = "about.html"
    
class CalendarView(TemplateView):
    template_name = "scheduler/calendar.html"
    
class TeamIndexView(generic.ListView):
    template_name = 'scheduler/teams.html'
    context_object_name = 'active_teams'

    def get_queryset(self):
        """Return all of the scheduler."""
        return Team.objects.all();
    
class PlayerIndexView(generic.ListView):
    template_name = 'scheduler/players.html'
    context_object_name = 'active_players'

    def get_queryset(self):
        """Return all of the players."""
        return Player.objects.all();

class TeamDetailView(generic.DetailView):
    model = Team
    template_name = 'scheduler/team_details.html'
    
class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'scheduler/player_details.html'    
    

