# 1.Overview
----
![alt tag](resource/image2015-9-16%2013-38-19.png)
- 1.JIRA 's comment-update event can be sent by `Webhook` via a `POST` request
- 2.Flask works as a proxy that get events from JIRA then send it to slack(in json format)
- 3.Slack Incoming WebHooks will handler the request and output in slack channel

Find me at [github-repo](https://github.com/smartxworks/jira-comment-slack)
Find original repo at [original-repo](https://github.com/Kisung/jira-comment-slack)

# 2. Environment
----
## 1. Create Slack Incoming Webhooks info
- Slack > Configure Integrations > Incoming Webhooks> View
![alt tag](resource/image2015-9-16%2013-37-36.png)


- Then click "Add Incoming WebHooks Integration" and create a Webhooks to a channel
![alt tag](resource/image2015-9-16%2013-40-30.png) 


- You will get a Webhooks url, **copy it** and then we will use it  
![alt tag](resource/image2015-9-16%2013-43-23.png)


## 2. API Server Configuration
Requires:

> python 2.6 +

> flask 0.10.1

Then run following command in shell.

```bash
# setup
python setup.py

# configure
cp jira_comment_slack.conf.json.example /etc/jira_comment_slack.conf.json
vim /etc/jira_comment_slack.conf.json
#{
#  "slack_url": "https://hooks.slack.com/services/XXXXXXXXX/YYYYYYYYY/zzzzzzzzzzzzzzzzzzzzzzzz",
#  "channel": "#random",
#  "port": 11000   # the flask server port
#}

# run server
/usr/bin/jira-comment-slack-server
```

## 3. JIRA Webhook Settings
- JIRA > System Menu
![alt tag](resource/image2015-9-16%2013-44-59.png)

- Find the "WebHooks" setting
![alt tag](resource/image2015-9-16%2013-45-50.png)

- Click "Create WebHook" to create a new webhook
- Enter the name and Enter the **url** where our flask app running, just like `http://host:port/webhook`
- Events should be set to "Issue : updated"
![alt tag](resource/image2015-9-16%2013-49-17.png)


# 3.Working Example
----
1.JIRA Comment capture
![alt tag](resource/image2015-9-16%2013-52-42.png)


2.API Server Log capture
![alt tag](resource/image2015-9-16%2013-53-40.png)


3.Slack Channel message capture
![alt tag](resource/image2015-9-16%2013-54-34.png)


# 4.link
----
Slack Attachments - https://api.slack.com/docs/attachments

flask - flask.pocoo.org

JIRA Webhook - https://developer.atlassian.com/jiradev/jira-architecture/webhooks



