import customtkinter as ctk
from tkinter import messagebox
from urllib import parse

app = ctk.CTk()
app.title("YGW Login App")
app.geometry("400x200")
app.configure(fg_color="green")


username_form = ctk.CTkEntry(app, placeholder_text="Enter username")
username_form.focus()
username_form.pack(pady=20)
password_form = ctk.CTkEntry(app, placeholder_text="Enter password")
password_form.pack(pady=20)


def get_data():
    # escape the username and password
    username = username_form.get()
    password = password_form.get()
    username = parse.quote(str(username))
    password = parse.quote(str(password))
    return username, password, "Firebox-DB"


def get_payload():
    username, password, domain = get_data()
    if len(username) <= 1 or len(password) <= 1:
        messagebox.showerror("Error", "Username or password are empty")
        return
    # FORMAT: fw_username=*******&fw_password=*************fw_domain=Firebox-DB&action=fw_logon&fw_logon_type=logon&redirect=&lang=en-US
    return f"fw_username={username}&fw_password={password}&fw_domain={domain}&action=fw_logon&fw_logon_type=logon&redirect=&lang=en-US"
