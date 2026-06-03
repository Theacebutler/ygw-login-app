#!/usr/bin/env python3
import customtkinter as ctk
from utils.store_crad import load_crad, store_crad
from urllib import parse
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
    if payload == -1:
        return
    try:
        response = requests.post(
            "https://10.39.3.1:4100/wgcgi.cgi", data=payload, verify=False
        )
        if response.status_code == 200 or response.status_code == 302:
            result_label.configure(text="User login Successful")
        else:
            result_label.configure(text=response.text[:100])  # Display first 100 chars
        app.destroy()
    except Exception as e:
        result_label.configure(text=f"Error: {e}")
        print(e)


def get_data():
    # escape the username and password
    pass


def get_payload():
    username, password = "", ""
    domain = "Firebox-DB"
    print("username", username, "password", password)
    return f"fw_username={username}&fw_password={password}&fw_domain={domain}&action=fw_logon&fw_logon_type=logon&redirect=&lang=en-US"


app = ctk.CTk()
app.title("YGW Login App")
app.geometry("400x400")
app.configure(fg_color="green")

header = ctk.CTkLabel(app, text="YGW Login App", font=("Arial", 20, "bold"))
header.pack(pady=20)


def show_from():
    # delete_crad()
    username, password = load_crad()
    print("username", username, "password", password)
    if username is None or password is None or username == "" or password == "":
        username_label = ctk.CTkLabel(app, text="Username:", font=("Arial", 20, "bold"))
        username_label.pack(pady=5)

        username_form = ctk.CTkEntry(app, placeholder_text="Enter username")
        username_form.focus()
        username_form.pack(pady=5)

        password_label = ctk.CTkLabel(app, text="Password:", font=("Arial", 20, "bold"))
        password_label.pack(pady=5)

        password_form = ctk.CTkEntry(app, placeholder_text="Enter password")
        password_form.pack(pady=5)

        username = username_form.get()
        password = password_form.get()
        username = parse.quote(str(username))
        password = parse.quote(str(password))
        store_crad(username, password)
    else:
        print("Found creds.json file")
        print("username", username, "password", password)
        pass


show_from()

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=5)

btn = ctk.CTkButton(app, text="Login", command=login)
btn.pack(pady=20)

footer = ctk.CTkLabel(app, text="Made by Avi Butler", font=("monospace", 10, "bold"))
footer.pack(pady=20)


if __name__ == "__main__":
    app.mainloop()
