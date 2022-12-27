#Богданов Алексей Максимович_Ум-222
#Практическая работа 11

import json
import requests
from pprint import pprint
import tkinter as tk
from tkinter import *

root=Tk()
root.title("GitHub API Handler")
root.geometry('480x360')

def get_response():
    url = f"https://api.github.com/users/{name.get()}"
    user_data = requests.get(url).json()
    keys=['company', 'created_at','email', 'id', 'name', 'url']
    filtred_data={k:user_data[k] for k in keys}
    #with open ('filtred_data.json', 'w+') as output:
    #    output.write(json.dumps(filtred_data, indent=4))
    with open ('filtred_data.txt', 'w+') as output:
        output.write(str(filtred_data))

lbl=Label(root, text="Укажите имя пользователя: ")
name=Entry(root, width=10)
btn=Button(root, text='Клик', command=get_response)
lbl.grid(column=0, row=0)
name.grid(column=1, row=0)
btn.grid(column=2, row=0)


root.mainloop()



