import customtkinter as tk
import webbrowser as web

from customtkinter import CTkButton

# adding url variables
YT_URL = "https://www.youtube.com"
GOOGLE_NOTES_URL = "https://keep.google.com/"
VS_CODE_URL = "https://vscode.dev/"
PYTHON_DOCS_URL = "https://docs.python.org/3/"
C_PLUS_PLUS_URL = "https://learn.microsoft.com/en-us/cpp/?view=msvc-170"
STACKOVERFLOW_URL = "https://stackoverflow.com/"
GEMINI_URL = "https://gemini.google.com/app"

# open url
def open_url(url):
    web.open(url)

tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")

#making the app
app = tk.CTk()
app.title("Website Opener")
app.geometry("400x400")

# main label
title = tk.CTkLabel(master=app , text="Website Opener (for devs)" , font=("Arial", 30))
title.pack(pady=10)



# youtube button

youtube_btn = tk.CTkButton(master = app , text="Youtube",command=lambda: open_url(YT_URL))
youtube_btn.pack(pady=10)

#google keep button

google_notes_btn = tk.CTkButton(master = app , text="Google keep/notes",command=lambda: open_url(GOOGLE_NOTES_URL))
google_notes_btn.pack(pady=10)

# vscode button

vscode_btn = tk.CTkButton(master=app , text="Vscode",command=lambda: open_url(VS_CODE_URL))
vscode_btn.pack(pady=10)

# python documents button

python_docs_btn =  tk.CTkButton(master=app , text="Python docs",command=lambda: open_url(PYTHON_DOCS_URL))
python_docs_btn.pack(pady=10)

# c++ documents button

c_plus_plus_btn = tk.CTkButton(master=app , text = "C++ docs",command=lambda: open_url(C_PLUS_PLUS_URL))
c_plus_plus_btn.pack(pady=10)

# stackoverflow button

stack_over_flow_btn = tk.CTkButton(master=app , text="Stack Overflow",command=lambda: open_url(STACKOVERFLOW_URL))
stack_over_flow_btn.pack(pady=10)

# gemini

gemini_btn = tk.CTkButton(master=app , text="Gemini",command=lambda: open_url(GEMINI_URL))
gemini_btn.pack(pady=10)


app.mainloop()