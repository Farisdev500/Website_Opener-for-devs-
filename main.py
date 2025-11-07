import customtkinter as tk
import webbrowser as web

URLS = {
    "Youtube": "https://www.youtube.com",
    "Google Keep/Notes": "https://keep.google.com/",
    "Vscode": "https://vscode.dev/",
    "Python Docs": "https://docs.python.org/3/",
    "C++ Docs": "https://learn.microsoft.com/en-us/cpp/?view=msvc-170",
    "Stack Overflow": "https://stackoverflow.com/",
    "Gemini": "https://gemini.google.com/app"
}

def open_url(url):
    web.open(url)

tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

app = tk.CTk()
app.title("Website Opener")
app.geometry("400x400")

title = tk.CTkLabel(master=app, text="Website Opener (for devs)", font=("Arial", 30))
title.pack(pady=10)

for text, url in URLS.items():
    button = tk.CTkButton(master=app, text=text, command=lambda url=url: open_url(url))
    button.pack(pady=10)

app.mainloop()
