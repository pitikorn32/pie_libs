from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    PushMessageRequest,
    TextMessage,
    ApiException,
)
from .base import BaseNotification


class LineNotification(BaseNotification):
    def __init__(self, channel_access_token: str, to_user_id: str):
        super().__init__()

        self.channel_access_token = channel_access_token
        self.config = Configuration(access_token=channel_access_token)
        self.to_user_id = to_user_id

    def send_message(self, message: str):
        with ApiClient(self.config) as api_client:
            messaging_api = MessagingApi(api_client)

            # Create a TextMessage object
            message = TextMessage(text=message)

            try:
                # Sending the message
                messaging_api.push_message(PushMessageRequest(to=self.to_user_id, messages=[message]))
            except ApiException as e:
                print("Error:", e)
