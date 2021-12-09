from django.shortcuts import render
from .models import *
from django.db.models import Q


# Create your views here.

def player_search_view(request):
    if request.method == 'GET':
        return render(request, 'Search/player_search.html')
    elif request.method == 'POST':
        name = request.POST['name']
        team = request.POST['team']
        country = request.POST['country']
        result = Playertoteam.objects.values('player__firstname', 'player__familyname', 'player__shortname',
                                             'player__firstname_cn', 'player__familyname_cn', 'player__shortname_cn',
                                             'player__originname', 'player__yearofbirth', 'player__countryid__name_cn',
                                             'team__fullname_en', 'team__fullname_cn', 'team__type', 'num', 'pos',
                                             'type', 'time_join', 'time_leave')

        if not name.isspace():
            result = result.filter(Q(player__firstname__icontains=name) | Q(player__familyname__icontains=name) |
                                   Q(player__shortname__icontains=name) | Q(player__firstname_cn__icontains=name) |
                                   Q(player__familyname_cn__icontains=name) | Q(player__shortname_cn__icontains=name) |
                                   Q(player__originname__icontains=name))

        if not team.isspace():
            result = result.filter(Q(team__fullname_en__icontains=team) | Q(team__fullname_cn__icontains=team))

        if not country.isspace():
            result = result.filter(player__countryid__name_cn__icontains=country)

        return render(request, 'Search/player_search.html', locals())


def team_search_view(request):
    if request.method == 'GET':
        return render(request, 'Search/team_search.html')
    elif request.method == 'POST':
        team = request.POST['team']
        league = request.POST['league']
        country = request.POST['country']
        result = Teamtoleague.objects.values('team__fullname_en', 'team__fullname_cn', 'team__type',
                                             'team__countryid__name_cn', 'league__name', 'league__name_cn',
                                             'season_start', 'season_end')

        if not team.isspace():
            result = result.filter(Q(team__fullname_en__icontains=team) | Q(team__fullname_cn__icontains=team))

        if not league.isspace():
            result = result.filter(Q(league__name__icontains=team) | Q(league__name_cn__icontains=team))

        if not country.isspace():
            result = result.filter(team__countryid__name_cn__icontains=country)
        return render(request, 'Search/team_search.html', locals())

