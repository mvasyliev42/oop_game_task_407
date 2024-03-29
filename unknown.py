#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Mar 25, 2024 09:23:55 AM CET  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import requests
import json

_location = os.path.dirname(__file__)

import unknown_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("648x554+451+124")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.0, rely=0.0, relheight=0.987, relwidth=0.992)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="#000000")

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.235, rely=0.272, height=44, width=188)
        self.Label3.configure(activebackground="#d9d9d9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 9")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="#000000")
        self.Label3.configure(text='''Label''')

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.235, rely=0.428, height=54, width=232)
        self.Label4.configure(activebackground="#d9d9d9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 9")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="#000000")
        self.Label4.configure(text='''Label''')

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.987, relwidth=1.008)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.331, rely=0.314, height=63, width=156)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Username''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.331, rely=0.697, height=56, width=147)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Authorization''')
        self.Button1.configure(command= self.button_click)

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.28, rely=0.247, height=40, relwidth=0.343)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(selectbackground="#d9d9d9")
        self.Entry1.configure(selectforeground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.331, rely=0.494, height=51, width=144)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 9")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''Password''')

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.28, rely=0.428, height=40, relwidth=0.343)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 10")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="#000000")
        self.Entry2.configure(insertbackground="#000000")
        self.Entry2.configure(selectbackground="#d9d9d9")
        self.Entry2.configure(selectforeground="black")

        self.Frame4 = tk.Frame(self.top)
        self.Frame4.place(relx=-0.093, rely=0.0, relheight=1.128, relwidth=1.258)

        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#d9d9d9")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="#000000")

        self.Listbox1 = tk.Listbox(self.Frame4)
        self.Listbox1.place(relx=0.294, rely=0.096, relheight=0.355
                , relwidth=0.361)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="#000000")
        self.Listbox1.configure(selectbackground="#d9d9d9")
        self.Listbox1.configure(selectforeground="black")

        self.Entry3 = tk.Entry(self.Frame4)
        self.Entry3.place(relx=0.294, rely=0.464, height=40, relwidth=0.361)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="#000000")
        self.Entry3.configure(insertbackground="#000000")
        self.Entry3.configure(selectbackground="#d9d9d9")
        self.Entry3.configure(selectforeground="black")

        self.Button2 = tk.Button(self.Frame4)
        self.Button2.place(relx=0.294, rely=0.576, height=46, width=147)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#000000")
        self.Button2.configure(text='''Profile''')
        self.Button2.configure(command= lambda: self.Frame2.tkraise())

        self.Button3 = tk.Button(self.Frame4)
        self.Button3.place(relx=0.479, rely=0.576, height=46, width=147)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#000000")
        self.Button3.configure(text='''Close''')
        self.Button3.configure(command= lambda: exit())
        self.Frame1.tkraise()
    def button_click(self):
        logintext =  self.Entry1.get()
        passwordtext =  self.Entry2.get()
        result = requests.post("http://127.0.0.1:5000/api/auth", json.dumps({"username": logintext, "password": passwordtext}), headers={"Content-Type": "application/json"})
        jsonresult = result.json()
        if jsonresult["data"] == False:
            self.Label3.config(text="Login or password is wrong")
        else:
            self.Label3.config(text=jsonresult["data"][1])
        self.Frame4.tkraise()
        print(result.json())
        pool = requests.get('http://127.0.0.1:5000/api/rating')
        jsonpool = pool.json()
        for item in range(len(jsonpool)):
            self.Listbox1.insert(item, f"Username: {jsonpool[item]['username']}, Wins: {jsonpool[item]['count']}")
        print(jsonpool)
    # label.config(text="Введено: " + input_text)


def start_up():
    unknown_support.main()

if __name__ == '__main__':
    unknown_support.main()




