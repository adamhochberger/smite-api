import json
from datetime import datetime
import hashlib
import os

import requests
from dotenv import load_dotenv
from smite_api_wrapper.ApiMethods import SmiteApiMethods, get_api_as_url
from smite_api_wrapper.get_method_name_from_api import get_method_name_from_api

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
        formatted_string = SmiteApiMethods.CREATE_SESSION.format(**signature_dictionary)
        print(formatted_string)

        url = get_api_as_url(formatted_string)
        response = requests.get(url)
        response_dictionary = response.json()
        self.session_id = response_dictionary["session_id"]
        print(response_dictionary)

    def test_session(self):
        signature_dictionary = self.create_signature("testsession")

        formatted_string = SmiteApiMethods.TEST_SESSION.format(**signature_dictionary, session=self.session_id)

        url = get_api_as_url(formatted_string)
        print(requests.get(url).json())

    def test_items_api(self):
        signature_dictionary = self.create_signature(get_method_name_from_api(SmiteApiMethods.GET_ITEMS))
        signature_dictionary["languagecode"] = "1"
        formatted_string = SmiteApiMethods.GET_ITEMS.format(**signature_dictionary, session=self.session_id)

        url = get_api_as_url(formatted_string)

        active_items_list = []
        inactive_items_list = []

        for item in requests.get(url).json():
            if item["ActiveFlag"] == "y":
                active_items_list.append(item["DeviceName"])
            else:
                inactive_items_list.append(item["DeviceName"])

        # print("Active Items", active_items_list)
        # print("Inactive Items", inactive_items_list)

        formatted_json_string = json.dumps(requests.get(url).json(), indent=4)
        print(formatted_json_string)
