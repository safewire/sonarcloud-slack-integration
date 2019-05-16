FROM python:3.7.3-alpine

RUN apk --update --no-cache add curl && rm -rf /var/cache/apk/*

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./connector.py connector.py

EXPOSE 9090

ENV SLACK_SONAR_WEBHOOK_URL=http://slack.com

HEALTHCHECK --interval=5s --timeout=5s --retries=2 \
  CMD curl --silent --fail localhost:9090/monitor || exit 1

ENTRYPOINT ["python"]
CMD ["-u","-m","connector"]

