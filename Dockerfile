FROM python:2.7

MAINTAINER "yewton" <yewton@gmail.com>

COPY . /opt/jira-comment-slack
WORKDIR /opt/jira-comment-slack

RUN python setup.py install

CMD ["/opt/jira-comment-slack/run.sh"]
