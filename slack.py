import requests
import json


def send_message_to_slack_channel(text, color, author_name, author_icon,
                                  title, footer, footer_icon, priority):
    data = {
        "text": text,
        "attachments": [
            {
                "title": title,
                "author_name": author_name,
                "color": color,
                "author_icon": author_icon,
                "footer": footer,
                "footer_icon": author_icon,
                "fields": [
                    {
                        "title": "Priority",
                        "value": priority,
                        "short": "false"
                    }
                ]
            },
        ]
    }
    headers = {'Content-type': 'application/json'}
    requests.post(
        "YOUR_SLACK_HOOK_URL",
        data=json.dumps(data),
        headers=headers
    )


send_message_to_slack_channel(text="Your text here",
                              color="#00FF00",
                              author_name="Your app name",
                              author_icon="http://i.imgur.com/OJkaVOI.jpg?1",
                              title="Your message Here",
                              footer="Footer",
                              footer_icon="http://a.slack-edge.com/7f18https://a.slack-edge.com/bfaba/img/api/homepage_custom_integrations-2x.png",
                              priority="high")
