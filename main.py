import os
from datetime import datetime

import requests
from dotenv import load_dotenv
import hashlib

load_dotenv()


def create_signature(method_name: str):
    dev_id = os.getenv("DEV_ID")
    auth_key = os.getenv("AUTH_KEY")
    current_datetime = datetime.utcnow()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")  # Datetime formatted as 'yyyyMMddHHmmss'

    string_to_hash = f"{dev_id}{method_name}{auth_key}{formatted_datetime}"
    hashed_string = hashlib.md5(string_to_hash.encode())

    signature_dictionary = {
        "developerId": dev_id,
        "authkey": auth_key,
        "signature": hashed_string.hexdigest(),
        "timestamp": formatted_datetime,
        "ResponseFormat": "Json"
    }

    return signature_dictionary


def create_session():
    signature_dictionary = create_signature("createsession")
    command_string = "/createsessionjson/{developerId}/{signature}/{timestamp}"
    formatted_command = command_string.format(**signature_dictionary)
    print(formatted_command)

    full_url = "https://api.smitegame.com/smiteapi.svc" + formatted_command
    response = requests.get(full_url)
    response_dictionary = response.json()
    session_id = response_dictionary["session_id"]
    print(response_dictionary)
    return session_id


def test_session(session_id: str):
    signature_dictionary = create_signature("testsession")

    base_string = "/testsession{ResponseFormat}/{developerId}/{signature}/{session}/{timestamp}"
    formatted_string = base_string.format(**signature_dictionary, session=session_id)

    url = "https://api.smitegame.com/smiteapi.svc" + formatted_string
    print(requests.get(url).json())


if __name__ == '__main__':
    session_id = create_session()
    test_session(session_id)
