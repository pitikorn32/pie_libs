import json
from httplib2 import Http
from .base import BaseNotification


class GoogleChatNotification(BaseNotification):
    def __init__(self, webhook_url: str):
        super().__init__()
        self.webhook_url = webhook_url

    def send_message(self, message: str):
        http_obj = Http()
        response = http_obj.request(
            uri=self.webhook_url,
            method="POST",
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps({"text": message}),
        )
        return response
