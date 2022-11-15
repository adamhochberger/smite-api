import os
from datetime import datetime

import requests
from dotenv import load_dotenv
import hashlib

load_dotenv()


class SmiteApiSessionManager:
    def __init__(self):
        self.dev_id = None
        self.auth_key = None
        self.session_id = None

        self._reload_dev_id_and_auth_key()

    def _reload_dev_id_and_auth_key(self):
        self.dev_id = os.getenv("DEV_ID")
        self.auth_key = os.getenv("AUTH_KEY")

    def create_signature(self, method_name: str):
        current_datetime = datetime.utcnow()
        formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")  # Datetime formatted as 'yyyyMMddHHmmss'

        signature_dictionary = {
            "developerId": self.dev_id,
            "authKey": self.auth_key,
            "timestamp": formatted_datetime,
            "ResponseFormat": "Json"
        }

        base_string_to_hash = "{developerId}{methodName}{authKey}{timestamp}"
        string_to_hash = base_string_to_hash.format(**signature_dictionary, methodName=method_name)
        hashed_string = hashlib.md5(string_to_hash.encode())
        signature_dictionary["signature"] = hashed_string.hexdigest()

        return signature_dictionary

    def create_session(self):
        signature_dictionary = self.create_signature("createsession")
        command_string = "/createsessionjson/{developerId}/{signature}/{timestamp}"
        formatted_command = command_string.format(**signature_dictionary)
        print(formatted_command)

        full_url = "https://api.smitegame.com/smiteapi.svc" + formatted_command
        response = requests.get(full_url)
        response_dictionary = response.json()
        self.session_id = response_dictionary["session_id"]
        print(response_dictionary)

    def test_session(self):
        signature_dictionary = self.create_signature("testsession")

        base_string = "/testsession{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
        formatted_string = base_string.format(**signature_dictionary, session=self.session_id)

        url = "https://api.smitegame.com/smiteapi.svc" + formatted_string
        print(requests.get(url).json())
