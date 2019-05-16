#!/usr/bin/env python3
import json
import os

import requests
from bottle import route, run, request

SLACK_SONAR_WEBHOOK_URL = os.environ["SLACK_SONAR_WEBHOOK_URL"]


@route('/sonarqube', method='POST')
def sonarqube():
    postdata = json.loads(request.body.read())

    result = "OK"
    if postdata['qualityGate']['status'] == "ERROR":
        text = f"{postdata['project']['name']} is failing the quality gate. " \
            f"\n\nBetter go check it out <{postdata['branch']['url']}> "
        response = requests.post(SLACK_SONAR_WEBHOOK_URL,
                                 data=json.dumps({"text": text}), headers={'Content-type': 'application/json'})
        result = response.text
    return result


@route('/monitor')
def monitor():
    return "OK"


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='0.0.0.0', port=9090, debug=True)
