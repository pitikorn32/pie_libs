from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    PushMessageRequest,
    TextMessage,
    ApiException,
)


class LineNotification:
    def __init__(self, channel_access_token: str):
        self.channel_access_token = channel_access_token
        self.config = Configuration(access_token=channel_access_token)

    def send_message(self, to_user_id: str, message: str):
        with ApiClient(self.config) as api_client:
            messaging_api = MessagingApi(api_client)

            # Create a TextMessage object
            message = TextMessage(text=message)

            try:
                # Sending the message
                messaging_api.push_message(PushMessageRequest(to=to_user_id, messages=[message]))
            except ApiException as e:
                print("Error:", e)
