import tkinter as tk
import requests
import json


def button_click():
    logintext = login.get()
    passwordtext = password.get()
    result = requests.post("http://127.0.0.1:5000/api/auth", json.dumps({"username": logintext, "password": passwordtext}), headers={"Content-Type": "application/json"})
    jsonresult = result.json()
    if jsonresult["data"] == False:
        label.config(text="Login or password is wrong")
    else:
        label.config(text=jsonresult["data"][2])
    print(result.json())
    # label.config(text="Введено: " + input_text)


window = tk.Tk()
window.title("Game")
# window.geometry("500x500")

# Створення текстового поля для вводу
login = tk.Entry(window, width=40)
password = tk.Entry(window, width=40)



login.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
password.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
# columnspan вказує, щоб поле вводу займало 3 стовпці
# padx і pady вказують на відступи навколо поля вводу
# sticky вказує, щоб поле вводу розтягнулося по горизонталі від лівого до правого краю


# Створення мітки для виведення введеного тексту
label = tk.Label(window, text="", width=40, bg="lightgray", padx=10, pady=5)

label.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

# Створення кнопки для виклику функції button_click
button = tk.Button(window, text="Authorize", command=button_click, width=10, bd=3, relief="raised")

button.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
# bd вказує на товщину рамки навколо кнопки
# relief вказує на стиль рамки кнопки


# Запуск головного циклу подій
window.mainloop()