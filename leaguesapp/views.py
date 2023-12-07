from django.shortcuts import render
from .models import League, Team
from django.contrib.auth.models import User, Permission
import csv

# Create your views here.

def home(request):
    #Open the leagues.csv file, which I downloaded into the project for simplicity sake
    f = open("/Users/t_nahod/usintegrityapp/usintegrity/leagues.csv")
    reader = csv.reader(f)
    #Iterate through the csv file
    for row in reader:
        #Get the different fields of each row in the csv file
        league_id = row[0]
        abbreviation = row[1]
        name = row[2]

        #Create a league object if it does not yet exist
        _, created = League.objects.get_or_create(
            league_id=league_id,
            abbreviation=abbreviation,
            name=name,
            )

    #Open the teams.csv file, which I downloaded into the project for simplicity sake
    f2 = open("/Users/t_nahod/usintegrityapp/usintegrity/teams.csv")
    reader2 = csv.reader(f2)
    #Iterate through the csv file
    for row in reader2:
        #Get the different fields of each row in the csv file
        abbreviation = row[0]
        name = row[1]
        league = League.objects.get(abbreviation = row[2])

        #Create a team object if it does not yet exist
        _, created = Team.objects.get_or_create(
            abbreviation=abbreviation,
            name=name,
            league=league
            )

    #Get all the leagues to pass as context to the front end
    leagues = League.objects.all()

    # user = User.objects.get(username= "newuser")
    # print(user.has_perm("add_league"))
    # add_perm = Permission.objects.get(codename="add_league")
    # user.user_permissions.add(add_perm)
    # user.save()
    # user = User.objects.get(username= "newuser")
    # print(user.has_perm("add_league"))
    # user.user_permissions.add(add_perm)


    #Render the page with relevant data
    return render(request,'pages/index.html', {"leagues" : leagues})

