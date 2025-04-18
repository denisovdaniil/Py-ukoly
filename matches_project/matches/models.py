from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.CASCADE)
    tournament = models.CharField(max_length=100)
    stadium = models.CharField(max_length=200)
    date = models.DateField()
    result = models.CharField(max_length=50) 
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} ({self.tournament})"

