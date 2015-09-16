# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
import json
import urllib2

app = Flask(__name__)

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
                "channel": "#jira-s_d",
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
            req = urllib2.Request('https://hooks.slack.com/services/XXXXXXXXX/YYYYYYYYY/zzzzzzzzzzzzzzzzzzzzzzzz')
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req, json.dumps(slack_data))
            app.logger.info(comment_body)

        data = jsonify(rd)
        return data
    else:
        app.logger.info(request)
        return "Done"


if __name__ == "__main__":
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)
