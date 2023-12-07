from django.db import models

# Create your models here.

class League(models.Model):
    league_id = models.IntegerField(blank=True, null=True)
    abbreviation = models.CharField(max_length = 5)
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.abbreviation

class Team(models.Model):
    abbreviation = models.CharField(max_length = 5)
    name = models.CharField(max_length = 50)
    league = models.ForeignKey(League, on_delete=models.CASCADE)