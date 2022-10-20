# importing required modules
from tkinter import *
import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.tix import Tk
from tkvideo import tkvideo
from PIL import ImageTk 
import PIL.Image
from facerec import *
from register import *
from face_detection  import *
from handler import *
import time
import csv
import pymysql
import ntpath
import os
from PIL import Image
import threading
import shutil
import numpy as np
from PIL import Image
from home import *
from home2 import *
from main_login import *


#------------------------------------------------------------ Main Window ----------------------------------------

window = tk.Tk()
window.title("Face-recognition challenge")
window.geometry("1300x900")
# Adding Background image to main window
bgg = PIL.Image.open("bg.png")
bgg = bgg.resize((1300, 900))
pimg = ImageTk.PhotoImage(bgg)

# adding label heading of my project
label = tk.Label(window,image=pimg)
label.place(x=0, y=0,width=1500, height=900)
tk.Label( text="Welcome to the Face Recognition Challenge For Microsoft Engage'22 👋", fg="#ffffff", highlightbackground="white", highlightthickness=4,
        font="Helvetica 25 bold", bg="#051729", pady=10).pack(padx=50, pady=20)


#  adding video to the Main window   
video_label = Label(window)
video_label.pack(padx=10,pady=10)
# read video to display on label
player = tkvideo("Face-recognition.mp4", video_label,loop = 1, size = (400, 200))
player.play()

# creating multiple windows using buttons and calling the funtion of files
b1 = Button(window, text="Login/Sign-Up",command=mainfunction,width=17, fg="#ffffff",
      pady=15, bd=0,highlightbackground="#051729", highlightthickness=4,font="Verdana 20 bold")
b2 = Button(window, text="Criminal-Detection 🕵️‍♀️", bg="white",command=home,width=17, fg="#ffffff",
      pady=15, bd=0,  highlightbackground="#051729", highlightthickness=4,font="Verdana 20 bold")
b3 = Button(window ,text="Find Missing People 🔎", command=home2,width=17, fg="#ffffff",
      pady=15, bd=0,highlightbackground="#051729", highlightthickness=4,bg="#ffffff",font="Verdana 20 bold")
b1.pack(pady=30)
b2.pack(pady=30)
b3.pack(pady=30)


# creating functions for my different social media handles
def callback():
      webbrowser.open_new_tab("https://twitter.com/MansiMi22804871")

def callback1():
      webbrowser.open_new_tab("https://github.com/0904-mansi")

def callback2():
      webbrowser.open_new_tab("https://www.linkedin.com/in/mansi-mishra-5435441b8/")

def callback3():
      webbrowser.open_new_tab("https://www.instagram.com/m_ansi_0904/")

# adding logos for my different social media handles
logo = ImageTk.PhotoImage(file = "linkedin.jpg")
tk.Button(window, image=logo, bg ="#051729", highlightbackground="#051729", highlightthickness=2, command=callback2).place(x=30,y=200)

logo1 = ImageTk.PhotoImage(file = "insta.jpg")
tk.Button(window, image=logo1, bg ="#051729", highlightbackground="#051729", highlightthickness=0,command=callback3 ).place( x=30,y=300)

logo2 = ImageTk.PhotoImage(file = "github.jpg")
tk.Button(window, image=logo2,bg ="#051729", highlightbackground="#051729", highlightthickness=0,command=callback1).place(x=30,y=400)

logo3 = ImageTk.PhotoImage(file = "twitter.jpg")
tk.Button(window, image=logo3,bg ="#051729",highlightbackground="#051729", highlightthickness=2, command=callback).place(x=30,y=500)


# adding my name
tk.Label(text="Developed By :" , fg="white",font="Verdana 20 bold",highlightbackground="#051729",bg="#051729", highlightthickness=4).pack(pady=20)
tk.Label(text="Mansi Mishra (Microsoft Engage'22 Mentee)" , fg="white",font="Verdana 20 bold",highlightbackground="#051729",bg="#051729", highlightthickness=4, ).pack(pady=10)

window.mainloop()
