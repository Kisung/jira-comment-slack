# -*- coding: utf-8 -*-
import pprint
from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
import json
import requests

app = Flask(__name__)

try:
    config = json.load(open("/etc/jira_comment_slack.conf.json", "r"))
    slack_url = config['slack_url']
    slack_channel = config['channel']
    flask_port = config["port"]
except IOError:
    raise IOError("Open config file error, please create new config file.")


@app.route('/webhook', methods=['GET', 'POST'])
def tracking():
    if request.method == 'POST':
        rd = request.get_json()
        if 'comment' in rd:
            comment_body = rd['comment']['body']
            comment_auther = rd['comment']['updateAuthor']['displayName']
            comment_id = rd['comment']['id']

            if rd['comment']['created'] == rd['comment']['updated']:
                comment_type = 'created'
                slack_color = "#439FE0"
            else:
                comment_type = 'updated'
                slack_color = "#7CD197"

            task_key = rd['issue']['key']
            task_id = rd['issue']['id']
            task_link = str(rd['issue']['self']).replace('rest/api/2/issue', 'browse').replace(task_id, task_key)
            task_summary = rd['issue']['fields']['summary']

            comment_link = task_link + "?focusedCommentId=%s&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-%s" % (comment_id, comment_id)

            slack_pretext = comment_auther + ' ' + comment_type + ' comment'
            slack_title = task_key + " : " + task_summary
            slack_data = {
                "username": "JIRA Comment ",
                "channel": slack_channel,
                "attachments": [
                    {
                        "fallback": slack_pretext + " - " + slack_title + " - " + comment_link,
                        "pretext": slack_pretext,
                        "title": slack_title,
                        "title_link": comment_link,
                        "text": comment_body,
                        "color": slack_color
                    }
                ]
            }
            response = requests.post(
                slack_url, data=json.dumps(slack_data),
                headers={'Content-Type': 'application/json'}
            )
            app.logger.info(comment_body)
            if response.status_code != 200:
                raise ValueError(
                    "Request to slack meets error %s, the response is:\n%s"
                    % (response.status_code, response.text)
                )

        data = jsonify(rd)
        return data
    else:
        app.logger.info(request)
        return "It Works!"


def main():
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True, host='0.0.0.0', port=flask_port, passthrough_errors=True)


if __name__ == "__main__":
    main()