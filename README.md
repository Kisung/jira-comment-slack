# 1.Overview
----
- 1.JIRA 이슈에 Comment가 등록/수정시 Webhook 설정에 등록된 URL로 POST 호출을 한다.
- 2.Flask로 구성된 REST API에서는 Post를 통해 들어온 JSON을 파싱하여 Slack API를 호출한다.
- 3.Slack Incoming WebHooks에 설정된 채널로 메세지를 전송한다.



# 2. Environment
----
## 1.Slack Incoming Webhooks 설정
- Slack > Integrations 설정 화면 하단의 DIY Integrations & Customizations에 있는 Incoming Webhooks의 View 버튼을 클릭한다.

- 메세지를 게시할 채널을 선택하고 "Add Incoming WebHooks Integration"버튼을 클릭하여 Hook을 생성한다.

- 상세 설정을 하고 자동 생성된 "Webhook URL"을 복사해둔다.


## 2. API Server 개발
개발 환경

> python 2.7

> flask 0.10.1

> AWS ELB + Ubuntu 14.04 EC2


## 3. JIRA Webhook 설정
- JIRA > System 설정 페이지로 이동

- 좌측메뉴 하단의 "WebHooks" 메뉴 클릭

- 화면 우측 상단의 "Create WebHook" 버튼을 클릭하여 신규 WebHook 생성 페이지로 이동.

- URL 항목에는 Flask로 구성한 API URL을 등록한다.

- Events 항목은 "Issue : updated"를 선택한다.


# 3.Work
----
1.JIRA Comment 등록

2.API Server Log 확인

3.Slack Channel message 확인

4.Message 링크 확인
메세지의 링크 클릭시 해당 이슈의 코멘트로 포커싱 되는것을 확인 한다.

# 4.link
----
Slack Attachments - https://api.slack.com/docs/attachments

flask - flask.pocoo.org

JIRA Webhook - https://developer.atlassian.com/jiradev/jira-architecture/webhooks




