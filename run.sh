#!/bin/bash -e

: ${HOST:=0.0.0.0}
: ${PORT:=11000}
: ${LOGFILE:=/var/log/jira_comment_slack.log}

cat << EOF > /etc/jira_comment_slack.conf.json
{
  "slack_url": "${SLACK_URL}",
  "channel": "${CHANNEL}",
  "host": "${HOST}",
  "port": "${PORT}",
  "logfile": "${LOGFILE}"
}
EOF

/usr/local/bin/jira-comment-slack-server
