# Sonarcloud / Sonarqube Slack Integration

This is a very simple bottle based python 3 application meant to re-format requests from sonarcub/sonarcloud into slack 
messages.  Once in a slack message it will be posted to the slack custom webhook for display.

Need to set the following environment variables:

APP_LOCATION should be set to 'heroku' when running on 'heroku'

SLACK_SONAR_WEBHOOK_URL should point to your https://hooks.slack.com/services/ABC... url

Clone this repo and then deploy it to heroku.  Works like a champ.


