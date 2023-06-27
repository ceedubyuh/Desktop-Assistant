# Written by Carter Womack
# Designed as an all-in-one Desktop Assistant application
# TODO: 
#   Get basic functions to work with command-line or hardcoding:
#       -Open and close applications
#       -Search Google
#       -Time and Date
#       -Control the system (sleep, shut down, restart)
#   Add a GUI so it"s accessible like an app
#   Make it hideable in taskbar
#   Keep it small and clean

from AppOpener import run
import webbrowser, requests
from bs4 import BeautifulSoup
import pystray
from pystray import MenuItem as item
from tkinter import *
from time import strftime
from PIL import Image
import os

root = Tk()
root.title("Personal Assistant")
root.geometry("1000x1000")
# Centering elements
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_propagate(False)

# Window Functions
def quitWindow(icon, item):
    icon.stop()
    root.destroy()

def showWindow(icon, item):
    icon.stop()
    root.after(0,root.deiconify)

def withdrawWindow():
    root.withdraw()
    img = Image.open("Desktop-Assistant/images/logo.png")
    menu = (item("Quit", quitWindow), item("Show", showWindow))
    icon = pystray.Icon("name", img, "title", menu)
    icon.run()

def minimizeWindow():
    root.iconify()
    img = Image.open("Desktop-Assistant/images/logo.png")
    menu = (item("Quit", quitWindow), item("Show", showWindow))
    icon = pystray.Icon("name", img, "title", menu)
    icon.run()

root.protocol("WM_DELETE_WINDOW", withdrawWindow)
# -------------------------------------------------Main FUNCTIONS ---------------------------------------------
# TIME
def currTime():
    current = strftime("%H:%M:%S %p")
    clock.config(text=current)
    clock.after(1000,currTime)

clock = Label(root, font=("calibri", 20, "bold"), foreground="black")
clock.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")
currTime()

#Search engine functionality
#Takes user input and parses their input into a google search
#It then opens the first google result of their input
text=StringVar()
def search():
    data = requests.get("https://www.google.com/search?q=" + text.get())
    soup =  BeautifulSoup(data.content, "html.parser")
    result =  soup.select(".kCrYT a")
    for link in result[:1]:
        searching = link.get("href")
        searching = searching[7:]
        searching = searching.split("&")
        webbrowser.open(searching[0])

label=Label(text="Search:",font=("Arial",15,"bold"))
label.grid(row=1,column=0, sticky="e")
enter=Entry(textvar=text,width=35)
enter.grid(row=1,column=1, sticky="ew")
button=Button(text="Search",width=20,command=search)
button.grid(row=1,column=2, padx=5, pady=5, sticky="w")
root.bind("<Return>", (lambda event: search()))


#SYSTEM CONTROLS
def restartPC():
    os.system("shutdown /r /t 0")

def sleepPC():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def shutdownPC():
    os.system("shutdown /s /t 0")

#Icons for System Control Icons
restartIcon = PhotoImage(file="Desktop-Assistant/images/restart.png")
sleepIcon = PhotoImage(file="Desktop-Assistant/images/sleep.png")
powerIcon = PhotoImage(file="Desktop-Assistant/images/power.png")

centerFrame = Frame(root)
centerFrame.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure((0, 1, 2), weight=1)

buttonFrame = Frame(centerFrame)
buttonFrame.pack()

#Buttons for System Control
restartButton = Button(buttonFrame, image=restartIcon, command=restartPC)
restartButton.grid(row=4, column=0, padx=5, pady=5)
sleepButton = Button(buttonFrame, image=sleepIcon, command=sleepPC)
sleepButton.grid(row=4, column=1, padx=5, pady=5)
shutdownButton = Button(buttonFrame, image=powerIcon, command=shutdownPC)
shutdownButton.grid(row=4, column=2, padx=5, pady=5)

# Lock the buttonFrame to the bottom-middle of the screen
centerFrame.grid_rowconfigure(0, weight=1)
centerFrame.grid_columnconfigure(0, weight=1)
buttonFrame.grid(sticky="s", pady=(0, 10))

#APPLIATION CONTROL
def openGoogle():
    google = "https://www.google.com"
    webbrowser.open(google)

def openSteam():
    run("steam")

#Icons for Application Buttons
googleIcon = PhotoImage(file="Desktop-Assistant/images/google.png")
steamIcon = PhotoImage(file="Desktop-Assistant/images/steam.png")
#Application Buttons
googleButton = Button(buttonFrame, image = googleIcon, command = openGoogle)
googleButton.grid(row=3, column=0, padx=(0, 5), sticky="nsew")
steamButton = Button(buttonFrame, image = steamIcon, command = openSteam)
steamButton.grid(row=3, column=1, padx=(5, 0), sticky="nsew")
mainloop()


