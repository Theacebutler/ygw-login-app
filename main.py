#!/usr/bin/env python3
from src.window import app, get_payload
import customtkinter as ctk
import requests
from dotenv import load_dotenv

load_dotenv()


def logout():
    # NOTE: Use this logout method for testing and developing only, it should not be used
    # in prod
    data = "Logout=Logout&action=fw_logon&fw_logon_type=logout"
    try:
        response = requests.post(
            "https://10.39.3.1:4100/wgcgi.cgi", data=data, verify=False
        )
        print(response.status_code)
    except Exception as e:
        print(e)


def login():
    payload = get_payload()
    try:
        response = requests.post(
            "https://10.39.3.1:4100/wgcgi.cgi", data=payload, verify=False
        )
        if response.status_code == 200 or response.status_code == 301:
            result_label.configure(text="User login Successful")
        else:
            result_label.configure(text=response.text[:100])  # Display first 100 chars
    except Exception as e:
        result_label.configure(text=f"Error: {e}")
        print(e)


btn = ctk.CTkButton(app, text="Login", command=login)
btn.pack(pady=20)

test_btn = ctk.CTkButton(app, text="TEST: logout", command=logout)
test_btn.pack(pady=40)

result_label = ctk.CTkLabel(app, text="Result will appear here")
result_label.pack(pady=20)


if __name__ == "__main__":
    app.mainloop()
