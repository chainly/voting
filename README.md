# voting ![travis-ci](https://travis-ci.com/chainly/voting.svg?branch=master)
simple voting application

# Project Description
```
Project Description
You are to build a simple web based voting application that allows a web user to vote on the following question:
What is the best video game of all time?
with the following options as possible answers:
•	Overwatch
•	World of Warcraft
•	PUBG
•	League of Legends

Project Requirements
Requirements for the voting application should:
•	Allow the web user to select only one answer.
•	Should only allow the web user to submit one vote per 24 hour period.
•	After the web user submits a vote, display the current results of the vote.

Project Instructions
1.	Build the voting application with whatever technology stack you want.
2.	Please include instructions on how to build/demo your application.
3.	Email the completed application with all the source code as a zip file to: rwang@doocai.cn

Project Notes
Things to keep in mind:
•	Please do not spend more than 8 hours building this application.
•	Do not worry about how the voting application actually looks in your browser. We are only looking at your back end programming skills.
•	This is your chance to show off what you can do.

Good luck!!
```

# Usage
- install: `pip install -r ./voting/requriments.txt`
- test: `python ./voting/manage.py test`
- createsuperuser: `python ./voting/manage.py createsuperuser`
- runserver: `python ./voting/manage.py runserver`
- about user: log in admin (http://127.0.0.1:8000/accounts/)
- about data: http://127.0.0.1:8000/api/
- aboot vote: http://127.0.0.1:8000/web/vote

# TODO
- cache api
- mysql transaction
- ajax
