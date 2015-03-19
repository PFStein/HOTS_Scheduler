from django.db import models

class Team(models.Model):
    '''
    This model represents a single Heroes of the Storm team
    It includes a tuple containing possible regions.
    The following models reference this model:
    Player, Event, Registrations
    '''
    UNITED_STATES = "USA"
    EUROPE = "EUR"
    REGION_CHOICES = (
          (UNITED_STATES, "The United States"),
          (EUROPE, "Europe")
    )
    team_name = models.CharField(max_length=50,unique=True)
    region = models.CharField(max_length=3,choices=REGION_CHOICES)
    
    def __str__(self):
        return self.team_name
    
    
class Role(models.Model):
    '''
    This model represents a named role on a single
    Heroes of the Storm team.
    This table exists so that players on a team can
    have multiple roles. Ex: (Manager and Player)
    This table will also determine permissions for 
    scheduling events.
    '''
    PLAYER = 'PL'
    TEAM_CAPTAIN = 'TC'
    MANAGER = 'MA'
    ANALYST = 'AN'
    ROLE_CHOICES = (
        (PLAYER, 'Player'),
        (TEAM_CAPTAIN, 'Team Captain'),
        (MANAGER, 'Manager'),
        (ANALYST, 'Analyst'),
    ) 
    name = models.CharField(max_length=2,
                            choices=ROLE_CHOICES,
                            default=PLAYER)
    def __str__(self):
        return self.name
    
    
class Player(models.Model):
    '''
    This is the main user Model for the website.
    This will contain relevant login information, team
    association, and role given to that player.
    '''
    email = models.EmailField(max_length=254,unique=True)
    player_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    team = models.ForeignKey(Team)
    roles = models.ManyToManyField(Role)     
    
    def __str__(self):
        return self.player_name
    
    
class Event(models.Model):
    '''
    This will be the main posting that a team can create.
    '''
    event_name = models.CharField(max_length=50)
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    hosting_team = models.ForeignKey(Team)
    
    def __str__(self):
        return "Name: {} | Start time: {} | End Time: {}".format(
                self.event_name,self.start_time,self.end_time)

class Registration(models.Model):
    '''
    Join table between Events and Teams signing up.
    Includes a specific start and end time.
    '''
    away_team = models.ForeignKey(Team)
    start_time = models.DateTimeField('Start Time')
    end_time = models.DateTimeField('End Time')
    event = models.ForeignKey(Event)
        
    
