from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from scheduler.models import Team,Player,Role,Event,Registration

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Role)
admin.site.register(Event)
admin.site.register(Registration)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PlayerInline(admin.StackedInline):
    model = Player
    can_delete = False
    
# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (PlayerInline, )

# Re-register UserAdmin    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)