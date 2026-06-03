# save the username and password to a json file
import json
import os

FILE_PATH = "creds.json"


def store_crad(username: str, password: str):
    with open(FILE_PATH, "w") as f:
        json.dump({"username": username, "password": password}, f)


def load_crad() -> tuple[str | None, str | None]:
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            return data["username"], data["password"]
    except FileNotFoundError:
        print("No creds.json file found")
    return "", ""


def delete_crad():
    try:
        os.remove(FILE_PATH)
        print(f"Deleted {FILE_PATH}")
    except FileNotFoundError:
        print(f"No {FILE_PATH} file found")
