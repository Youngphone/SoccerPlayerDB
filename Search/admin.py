from django.contrib import admin
from .models import *


# Register your models here.
class CountryManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_cn']
    list_display_links = ['name']
    search_fields = ['name', 'name_cn']


class LeagueManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'name_cn', 'countryid']
    list_display_links = ['name']
    search_fields = ['name', 'name_cn', 'countryid__name']


class TeamManager(admin.ModelAdmin):
    list_display = ['id', 'fullname_en', 'shortname_en', 'fullname_cn', 'shortname_cn', 'type', 'countryid']
    list_display_links = ['fullname_en']
    search_fields = ['fullname_en', 'fullname_cn', 'shortname_en', 'shortname_cn', 'countryid__name']
    list_filter = ['countryid']


class PlayerManager(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'shortname', 'full_name_cn', 'shortname_cn', 'originname', 'yearofbirth',
                    'countryid']
    list_display_links = ['full_name']
    search_fields = ['firstname', 'familyname', 'shortname', 'firstname_cn', 'familyname_cn', 'shortname_cn',
                     'originname', 'countryid__name']
    list_filter = ['countryid']


class TeamtoleagueManager(admin.ModelAdmin):
    list_display = ['id', 'team', 'league', 'season_start', 'season_end']
    list_display_links = ['team']
    search_fields = ['team__fullname_en', 'league__name']
    list_filter = ['league']


class PlayertoteamManager(admin.ModelAdmin):
    list_display = ['id', 'player', 'team', 'num', 'pos', 'type', 'time_join', 'time_leave']
    list_display_links = ['player']
    search_fields = ['player__firstname', 'player__familyname', 'team__fullname_en', 'pos']
    list_filter = ['team']
    raw_id_fields = ("player",)


admin.site.register(Country, CountryManager)
admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Players, PlayerManager)
admin.site.register(Teamtoleague, TeamtoleagueManager)
admin.site.register(Playertoteam, PlayertoteamManager)
