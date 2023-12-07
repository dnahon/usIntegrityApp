from django.contrib import admin
from leaguesapp.models import League, Team

# Register your models here.
class TeamInline(admin.TabularInline):
    model = Team

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    inlines = [
        TeamInline,
    ]