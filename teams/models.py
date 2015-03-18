from django.db import models

class Team(models.Model):
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
    email = models.EmailField(max_length=254,unique=True)
    player_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    team = models.ForeignKey(Team)
    roles = models.ManyToManyField(Role)     
    
    def __str__(self):
        return self.player_name
    
