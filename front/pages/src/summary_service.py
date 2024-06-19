import configparser
import re

import requests

config = configparser.ConfigParser()
config.read("config.ini")

SERVER_URL = config.get("DEV", "APP_URL")


async def create_chat(input_data):
    """
    Creates a new chat.

    :param input_data: The data to be sent to the server for chat creation.
    :return: The response from the server.
    """
    api_url = SERVER_URL + '/api/summarize/'
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(api_url, json=input_data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"The request finished with an error {response.status_code}: {response.text}"
