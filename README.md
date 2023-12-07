# usIntegrityApp
This is a bare bones app that accomplishes a few things:
- It is a one page app that contains a brief welcome message, a link to the admin panel, and then displays tables of teams by league imported from CSV files
- It contains the league and team models
- It contains a LeagueAdmin model, with a Team inline, to allow admin users to modify team objects from within a league only

Relevant files are views.py, models.py, admin.py, and index.html
