import pymsteams
from .base import BaseNotification


class MSTeamsNotification(BaseNotification):
    """
    A class to send notifications to Microsoft Teams using a webhook URL.

    Attributes:
        webhook_url (str): The webhook URL for the Microsoft Teams channel.
        myTeamsMessage (pymsteams.connectorcard): The connector card object for sending messages.

    Methods:
        __init__(webhook_url: str):
            Initializes the MSTeamsNotification with the provided webhook URL.

        send_message(message: str, color: str = None):
            Sends a message to the Microsoft Teams channel.

            Args:
                message (str): The message to be sent.
                color (str, optional): The color of the message card. Defaults to None.
    """

    def __init__(self, webhook_url: str):
        super().__init__()

        self.webhook_url = webhook_url
        self.myTeamsMessage = pymsteams.connectorcard(webhook_url)

    def send_message(self, message: str, color: str = None):
        """
        Sends a message using the myTeamsMessage object.

        Args:
            message (str): The message to be sent.
            color (str, optional): The color to be used for the message. Defaults to None.

        Returns:
            None
        """
        self.myTeamsMessage.text(message)
        if color:
            self.myTeamsMessage.color(color)
        self.myTeamsMessage.send()
