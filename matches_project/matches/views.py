from django.shortcuts import render, redirect, get_object_or_404

from django import forms
from .models import Match, Team

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team1', 'team2', 'tournament', 'stadium', 'date', 'result', 'note']
    team1_logo = forms.ImageField(required=False)
    team2_logo = forms.ImageField(required=False)

def match_list(request):
    matches = Match.objects.all()
    return render(request, 'matches/match_list.html', {'matches': matches})

def add_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            match = form.save(commit=False)

            
            team1_logo = request.FILES.get('team1_logo')
            team2_logo = request.FILES.get('team2_logo')

            
            if team1_logo and not match.team1.logo:
                match.team1.logo = team1_logo
                match.team1.save()

            if team2_logo and not match.team2.logo:
                match.team2.logo = team2_logo
                match.team2.save()

            match.save()
            return redirect('match_list')
    else:
        form = MatchForm()
    
    teams = Team.objects.all()
    return render(request, 'matches/add_match.html', {'form': form, 'teams': teams})

def team_info(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    matches = Match.objects.filter(team1=team) | Match.objects.filter(team2=team)
    matches = matches.order_by('-date')

    return render(request, 'matches/team_info.html', {
        'team': team,
        'matches': matches
    })