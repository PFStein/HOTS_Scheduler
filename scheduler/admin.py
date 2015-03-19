from django.contrib import admin
from scheduler.models import Team,Player,Role,Event,Registration

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Role)
admin.site.register(Event)
admin.site.register(Registration)