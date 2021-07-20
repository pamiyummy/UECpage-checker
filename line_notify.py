import requests
import os


def line_notify(text: str) -> None:
    """lineのトーク画面にメッセージを送信する。

    Args:
        text (str): 送信したいメッセージ
    """
    line_notify_token = os.environ['LINE_NOTIFY_TOKEN']
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': text}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)
